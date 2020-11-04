"""
.. module:: akit.integration.agents.sshagent
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`SshAgent` class and associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import re
import socket
import stat
import time

from akit.aspects import RunPattern, DEFAULT_ASPECTS
from akit.exceptions import AKitInvalidConfigError

import paramiko

DEFAULT_SSH_TIMEOUT = 300
DEFAULT_SSH_RETRY_INTERVAL = .5

#                    PERMS          LINKS   OWNER       GROUPS    SIZE   MONTH  DAY  TIME    NAME
#                  rwxrwxrwx         24      myron      myron     4096   Jul    4   00:37  PCBs
REGEX_DIRECTORY_ENTRY = re.compile(r"([\S]+)[\s]+([0-9]+)[\s]+([\S]+)[\s]+([\S]+)[\s]+([0-9]+)[\s]+([A-za-z]+[\s]+[0-9]+[\s]+[0-9:]+)[\s]+([\S\s]+)")
def lookup_entry_type(pdir, ename, finfo):
    etype = None
    if stat.S_ISREG(finfo.st_mode):
        etype = "file"
    elif stat.S_ISDIR(finfo.st_mode):
        etype = "dir"
    elif stat.S_ISLNK(finfo.st_mode):
        etype = "link"
    elif stat.S_ISCHR(finfo.st_mode):
        etype = "char"
    elif stat.S_ISBLK(finfo.st_mode):
        etype = "block"
    else:
        print ("ERROR: Unknown entry type. pdir=%s, ename=%s" % (pdir, ename))

    return etype

def primitive_list_directory(ssh_client, directory):
    """
        Uses a primitive method to create a list of the files and folders in a directory
        by running the 'ls -al' commands on the directory.  This is required if the SSH
        server does not support sftp.
    """
    entries = None

    ls_cmd = "ls -al %s" % directory

    status, stdout, stderr = ssh_execute_command(ssh_client, ls_cmd)

    if status == 0:
        entries = primitive_parse_directory_listing(directory, stdout)
    else:
        # Allow permission denied errors
        if stderr.find("Permission denied") < 0:
            errmsg = "Error attempting to get a primitive directory listing.\n    CMD=%s\n    STDERR:\n%s" % (ls_cmd, stderr)
            raise Exception(errmsg)

    return entries

def primitive_list_tree(ssh_client, treeroot, max_depth=1):
    """
        Uses a primitive method to create an information tree about the files and folders
        in a directory tree by running 'ls -al' commands on the directory tree.  This is
        required if the SSH server does not support sftp.
    """
    
    level_items = primitive_list_directory(ssh_client, treeroot)

    if max_depth > 1:
        if not treeroot.endswith("/"):
            treeroot = treeroot + "/"

        for nxtitem in level_items.values():
            nxtname = nxtitem["name"]
            if nxtitem["type"] == "dir":
                nxtroot = treeroot + nxtname
                nxtchildren = primitive_list_tree_recurse(ssh_client, nxtroot, max_depth - 1)
                nxtitem.update(nxtchildren)

    tree_info = {
        "name": treeroot,
        "items": level_items
    }

    return tree_info

def primitive_list_tree_recurse(ssh_client, rootdir, remaining):

    level_items = primitive_list_directory(ssh_client, rootdir)

    if remaining > 1:
        if not rootdir.endswith("/"):
            rootdir = rootdir + "/"

        for nxtitem in level_items.values():
            nxtname = nxtitem["name"]
            if nxtitem["type"] == "dir":
                nxtroot = rootdir + nxtname
                nxtchildren = primitive_list_tree_recurse(ssh_client, nxtroot, remaining - 1)
                nxtitem.update(nxtchildren)

    children_info = {
        "items": level_items
    }

    return children_info

def primitive_parse_directory_listing(dir, content):
    """
        {
            "name": "blah",
            "type": "dir", # dir, file, link
            "owner": "root",
            "group": "root",
            "modified": "Jul  4 00:37"
            "size": 1234
        }
    """
    entries = {}

    listing_lines = content.splitlines(False)
    for nxtline in listing_lines:
        nxtline = nxtline.strip()

        mobj = REGEX_DIRECTORY_ENTRY.match(nxtline)
        if mobj is not None:
            mgroups = mobj.groups()

            name = mgroups[6]
            if name == "." or name == "..":
                continue

            perms = mgroups[0]

            perms_tc = perms[0]
            etype = None
            if perms_tc == '-':
                etype = "file"
            elif perms_tc == 'd':
                etype = "dir"
            elif perms_tc == 'l':
                etype = "link"
                name, _ = name.split(" -> ")
            elif perms_tc == 'c':
                etype = "char"
            elif perms_tc == 'b':
                etype = "block"
            else:
                raise Exception("Unknown directory listing entry type. dir=%s tc=%s" % (dir, perms_tc))

            dentry = {
                "name": name,
                "perms": perms,
                "type": etype,
                "owner": mgroups[2],
                "group": mgroups[3],
                "size": mgroups[4],
                "modified": mgroups[5]
            }

            entries[name] = dentry

    return entries

def primitive_pull_file(ssh_client, remotepath, localpath):

    copycmd = "cat %s" % remotepath

    status, stdout, stderr = ssh_execute_command(ssh_client, copycmd)

    if status != 0:
        raise Exception("Error pulling file using command. cmd=%s" % copycmd)

    with open(localpath, 'w') as lfile:
        lfile.write(stdout)

    return

def primitive_push_file(ssh_client, localpath, remotepath):
    raise Exception("primitive_push_file: not implemented")
    return

def sftp_list_directory(sftp, directory, userlookup, grouplookup):

    entries = {}

    try:
        sftp.chdir(directory)
        directory_items = sftp.listdir()

        for nname in directory_items:
            ninfo = sftp.lstat(nname)
            perms = ""
            dentry = {
                "name": nname,
                "perms": perms,
                "type": lookup_entry_type(directory, nname, ninfo),
                "owner": userlookup(ninfo.st_uid),
                "group": grouplookup(ninfo.st_gid),
                "size": ninfo.st_size,
                "accessed": ninfo.st_atime,
                "modified": ninfo.st_mtime
            }

            entries[nname] = dentry
    except PermissionError:
        pass

    return entries

def sftp_list_tree(sftp, treeroot, userlookup, grouplookup, max_depth=1):

    level_items = sftp_list_directory(sftp, treeroot, userlookup, grouplookup)

    if max_depth > 1:
        if not treeroot.endswith("/"):
            treeroot = treeroot + "/"

        for nxtitem in level_items.values():
            nxtname = nxtitem["name"]
            if nxtitem["type"] == "dir":
                nxtroot = treeroot + nxtname
                nxtchildren = sftp_list_tree_recurse(sftp, nxtroot, userlookup, grouplookup, max_depth - 1)
                nxtitem.update(nxtchildren)

    tree_info = {
        "name": treeroot,
        "items": level_items
    }

    return tree_info

def sftp_list_tree_recurse(sftp, rootdir, userlookup, grouplookup, remaining):

    level_items = sftp_list_directory(sftp, rootdir, userlookup, grouplookup)

    if remaining > 1:
        if not rootdir.endswith("/"):
            rootdir = rootdir + "/"

        for nxtitem in level_items.values():
            nxtname = nxtitem["name"]
            if nxtitem["type"] == "dir":
                nxtroot = rootdir + nxtname
                nxtchildren = sftp_list_tree_recurse(sftp, nxtroot, userlookup, grouplookup, remaining - 1)
                nxtitem.update(nxtchildren)

    children_info = {
        "items": level_items
    }

    return children_info

def ssh_execute_command(ssh_client, command, inactivity_timeout=DEFAULT_SSH_TIMEOUT, inactivity_interval=DEFAULT_SSH_RETRY_INTERVAL, chunk_size=1024):
    """
        Runs a command on a remote server using the specified ssh_client.  We implement our own version of ssh_execute_command
        in order to have better control over the timeouts and to make sure all the checks are sequenced properly in order
        to prevent SSH lockups.

        :param ssh_client: The :class:`paramiko.SSHClient` object to utilize when running the command.
        :type ssh_client: :class:`paramiko.SSHClient`
        :param command: The commandline to run.
        :type command: str
        :param inactivity_timeout: The timeout for the channel for the ssh transaction.
        :type inactivity_timeout: float
        :param inactivity_interval: The retry interval to wait for the channel to have data ready.
        :type inactivity_interval: float
        :param chunk_size: The size of the chunks that are read during receive operations
        :type chunk_size: int

        :returns: A tuple with the command result code, the standard output and the standard error output.
        :rtype: (int, str, str)
    """
    status = None
    stdout_buffer = bytearray()
    stderr_buffer = bytearray()

    start_time = time.time()
    end_time = start_time + inactivity_timeout

    channel = ssh_client.get_transport().open_session(timeout=inactivity_timeout)
    channel.exec_command(command)

    while True:
        # Grab exit status ready before checking to see if stdout_ready or stderr_ready are True
        exit_status_ready = channel.exit_status_ready()
        stdout_ready = channel.recv_ready()
        stderr_ready = channel.recv_stderr_ready()

        # If stdout_ready or stderr_ready are true, we read this round
        if stdout_ready or stderr_ready:
            if stdout_ready:
                rcv_data = channel.recv(chunk_size)
                stdout_buffer.extend(rcv_data)
            if stderr_ready:
                rcv_data = channel.recv_stderr(chunk_size)
                stderr_buffer.extend(rcv_data)

            # We only want to timeout if there is inactivity
            start_time = time.time()
            end_time = start_time + inactivity_timeout
        # If we did not ready any data this round and our exit status was ready, its time to exit
        elif exit_status_ready:
            status = channel.recv_exit_status()
            break
        # We didn't have any data to read and our exit status was not ready, go to sleep for interval
        else:
            now_time = time.time()
            if now_time > end_time:
                diff_time = now_time - start_time
                err_msg = "Timeout while executing SSH command.\n    command=%s\n    start=%r end=%r now=%r diff=%r" % (
                    command, start_time, end_time, now_time, diff_time)
                raise TimeoutError(err_msg)

            # If we did not timeout, go to sleep for the interval before we make another attempt to read
            time.sleep(inactivity_interval)

        # End while True

    stdout = stdout_buffer.decode()
    del stdout_buffer

    stderr = stderr_buffer.decode()
    del stderr_buffer

    return status, stdout, stderr

class SshSession:
    def __init__(self, host, username, password=None, keyfile=None, keypasswd=None, port=22, aspects=DEFAULT_ASPECTS):
        self._host = host
        self._ipaddr = socket.gethostbyname(host)
        self._port = port
        self._username = username
        self._password = password
        self._keyfile = keyfile
        self._keypasswd = keypasswd
        self._aspects = aspects
        self._ssh_client = None
        self._primitive_mode = False

        if self._password is None and self._keyfile is None:
            raise AKitInvalidConfigError("SshAgent requires either a 'password' or identity 'keyfile' be specified.")
        return

    def __enter__(self):
        self._ssh_client = self._create_client()
        return

    def __exit__(self, ex_val, ex_type, ex_tb):
        self._ssh_client.close()
        handled = False
        return handled

    def run_cmd(self, command, aspects=None):

        if aspects is None:
            aspects = self._aspects

        timeout=aspects.inactivity_timeout
        interval=aspects.inactivity_interval

        status = None
        stdout = None
        stderr = None

        if aspects.run_pattern == RunPattern.SINGLE_RUN:
            status, stdout, stderr = ssh_execute_command(self._ssh_client, command, inactivity_timeout=timeout, inactivity_interval=interval)

        elif aspects.run_pattern == RunPattern.RUN_UNTIL_SUCCESS:
            while True:
                status, stdout, stderr = ssh_execute_command(self._ssh_client, command, inactivity_timeout=timeout, inactivity_interval=interval)
                if status == 0:
                    break
                else:
                    pass

        elif aspects.run_pattern == RunPattern.RUN_WHILE_SUCCESS:
            while True:
                status, stdout, stderr = ssh_execute_command(self._ssh_client, command, inactivity_timeout=timeout, inactivity_interval=interval)
                if status != 0:
                    break
                else:
                    pass

        return status, stdout, stderr

    def _create_client(self):
        pkey = None
        if self._keyfile is not None:
            pkey = paramiko.pkey.PKey.from_private_key_file(self._keyfile, password=self._keypasswd)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(self._ipaddr, port=self._port, username=self._username, password=self._password, pkey=pkey)
        return ssh_client


class SshAgent:

    def __init__(self, host, username, password=None, keyfile=None, keypasswd=None, allow_agent=False, port=22, primitive=None, aspects=DEFAULT_ASPECTS):
        self._host = host
        self._ipaddr = socket.gethostbyname(self._host)
        self._port = port
        self._username = username
        self._password = password
        self._keyfile = keyfile
        self._keypasswd = keypasswd
        self._allow_agent = allow_agent
        self._aspects = aspects
        if primitive is None:
            self._primitive = True
        self._primitive = primitive

        self._user_lookup_table = {}
        self._group_lookup_table = {}

        if self._password is None and self._keyfile is None:
            raise AKitInvalidConfigError("SshAgent requires either a 'password' or identity 'keyfile' be specified.")
        return

    @property
    def allow_agent(self):
        return self._allow_agent

    @property
    def aspects(self):
        return self._aspects

    @property
    def host(self):
        return self._host

    @property
    def keyfile(self):
        return self._keyfile

    @property
    def keypasswd(self):
        return self._keypasswd

    @property
    def ipaddr(self):
        return self._ipaddr

    @property
    def password(self):
        return self._password

    @property
    def port(self):
        return self._port

    @property
    def username(self):
        return self._username

    def run_cmd(self, command, aspects=None, ssh_client=None):

        if aspects is None:
            aspects = self._aspects

        inactivity_timeout=aspects.inactivity_timeout
        inactivity_interval=aspects.inactivity_interval

        cleanup_client = False
        status = None
        stdout = None
        stderr = None
        try:
            if ssh_client is None:
                ssh_client = self._create_client()
                cleanup_client = True

            if aspects.run_pattern == RunPattern.SINGLE_RUN:
                status, stdout, stderr = ssh_execute_command(ssh_client, command, inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)

            elif aspects.run_pattern == RunPattern.RUN_UNTIL_SUCCESS:
                while True:
                    status, stdout, stderr = ssh_execute_command(ssh_client, command, inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)
                    if status == 0:
                        break
                    else:
                        pass

            elif aspects.run_pattern == RunPattern.RUN_WHILE_SUCCESS:
                while True:
                    status, stdout, stderr = ssh_execute_command(ssh_client, command, inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)
                    if status != 0:
                        break
                    else:
                        pass

        finally:
            if cleanup_client:
                ssh_client.close()
                del ssh_client

        return status, stdout, stderr

    def directory_tree(self, root_dir, depth=1, ssh_client=None):

        dir_info = {}

        cleanup_client = False
        try:
            if ssh_client is None:
                ssh_client = self._create_client()
                cleanup_client = True

            if not self._primitive:
                transport = ssh_client.get_transport()
                try:

                    sftp = paramiko.SFTPClient.from_transport(transport)
                    try:
                        dir_info = sftp_list_tree(sftp, root_dir, self.lookup_user_by_uid, self.lookup_group_by_uid, max_depth=depth)
                    finally:
                        sftp.close()
                finally:
                    transport.close()
            else:
                dir_info = primitive_list_tree(ssh_client, root_dir, max_depth=depth)

        except Exception as xcpt:
            raise
        finally:
            if cleanup_client:
                ssh_client.close()
                del ssh_client

        return dir_info

    def directory(self, root_dir, ssh_client=None):

        dir_info = {}

        cleanup_client = False
        try:
            if ssh_client is None:
                ssh_client = self._create_client()
                cleanup_client = True

            if not self._primitive:
                transport = ssh_client.get_transport()
                try:

                    sftp = paramiko.SFTPClient.from_transport(transport)
                    try:
                        dir_info = sftp_list_directory(sftp, root_dir, self.lookup_user_by_uid, self.lookup_group_by_uid)
                    finally:
                        sftp.close()
                finally:
                    transport.close()
            else:
                dir_info = primitive_list_directory(ssh_client, root_dir)

        except Exception as xcpt:
            raise
        finally:
            if cleanup_client:
                ssh_client.close()
                del ssh_client

        return dir_info

    def pull_file(self, remotepath, localpath, ssh_client=None):

        cleanup_client = False
        try:
            if ssh_client is None:
                ssh_client = self._create_client()
                cleanup_client = True
            
            if not self._primitive:
                transport = ssh_client.get_transport()
                try:
                    sftp = paramiko.SFTPClient.from_transport(transport)
                    try:
                        sftp.get(remotepath, localpath)
                    finally:
                        sftp.close()
                finally:
                    transport.close()
            else:
                primitive_pull_file(ssh_client, remotepath, localpath)

        except Exception as xcpt:
            raise
        finally:
            if cleanup_client:
                ssh_client.close()
                del ssh_client
    
        return

    def push_file(self, localpath, remotepath, ssh_client=None):

        cleanup_client = False
        try:
            if ssh_client is None:
                ssh_client = self._create_client()
                cleanup_client = True
            
            if not self._primitive:
                transport = ssh_client.get_transport()
                try:
                    sftp = paramiko.SFTPClient.from_transport(transport)
                    try:
                        sftp.put(localpath, remotepath)
                    finally:
                        sftp.close()
                finally:
                    transport.close()
            else:
                primitive_push_file(ssh_client, localpath, remotepath)

        except Exception as xcpt:
            raise
        finally:
            if cleanup_client:
                ssh_client.close()
                del ssh_client

        return

    def lookup_user_by_uid(self, uid, update=False):
        username = None

        if uid in self._user_lookup_table:
            username = self._user_lookup_table[uid]
        else:
            status, stdout, _ = self.run_cmd("id -n -u %d" % uid)
            if status == 0:
                username = stdout.strip()
                self._user_lookup_table[uid] = username

        return username

    def lookup_group_by_uid(self, gid, update=False):
        grpname = None

        if gid in self._group_lookup_table:
            grpname = self._group_lookup_table[gid]
        else:
            status, stdout, _ = self.run_cmd("id -n -g %d" % gid)
            if status == 0:
                grpname = stdout.strip()
                self._group_lookup_table[gid] = grpname

        return grpname
    
    def verify_connectivity(self):
        """
            Method that can be used to verify connectivity to the target computer.
        """
        vok = False

        hello_cmd = "echo Hello"
        status, stdout, stderr = self.run_cmd(hello_cmd)
        if status == 0 and stdout.strip() == "Hello":
            vok = True

        return vok

    def _create_client(self):
        pkey = None
        if self._keyfile is not None:
            with open(self._keyfile) as kf:
                pkey = paramiko.rsakey.RSAKey.from_private_key(kf, password=self._keypasswd)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(self._ipaddr, port=self._port, username=self._username, password=self._password, allow_agent=self._allow_agent, pkey=pkey)
        return ssh_client
