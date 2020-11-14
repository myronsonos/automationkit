"""
.. module:: sshagent
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
import threading
import time
import weakref

from typing import Callable, List, Optional, Sequence, Union

from akit.aspects import Aspects, LoggingPattern, RunPattern, DEFAULT_ASPECTS
from akit.exceptions import AKitInvalidConfigError, AKitNotOverloadedError

from akit.xlogging.foundations import getAutomatonKitLogger
from akit.xlogging.scopemonitoring import MonitoredScope

from akit.integration.landscaping.landscapedeviceextension import LandscapeDeviceExtension

import paramiko

logger = getAutomatonKitLogger()

DEFAULT_SSH_TIMEOUT = 300
DEFAULT_SSH_RETRY_INTERVAL = .5

DEFAULT_FAILURE_LABEL = "Failure"
DEFAULT_SUCCESS_LABEL = "Success"

TEMPLATE_COMMAND_FAILURE = "RUNCMD: {} running CMD=%s{}STDOUT:{}%s{}STDERR:{}%s{}".format(DEFAULT_FAILURE_LABEL, *([os.linesep] * 5))
TEMPLATE_COMMAND_SUCCESS = "RUNCMD: {} running CMD=%s{}STDOUT:{}%s{}STDERR:{}%s{}".format(DEFAULT_SUCCESS_LABEL, *([os.linesep] * 5))

#                    PERMS          LINKS   OWNER       GROUPS    SIZE   MONTH  DAY  TIME    NAME
#                  rwxrwxrwx         24      myron      myron     4096   Jul    4   00:37  PCBs
REGEX_DIRECTORY_ENTRY = re.compile(r"([\S]+)[\s]+([0-9]+)[\s]+([\S]+)[\s]+([\S]+)[\s]+([0-9]+)[\s]+([A-za-z]+[\s]+[0-9]+[\s]+[0-9:]+)[\s]+([\S\s]+)")
def lookup_entry_type(pdir: str, ename: str, finfo: paramiko.SFTPAttributes):
    """
        Determines the entry type labelto assign to a file entry based on the st_mode of the file information.

        :param pdir: The parent directory of the file, passed for logging purposes.
        :type pdir: str
        :param ename: The entry name of the file in the directory listing.
        :type ename: str
        :param finfo: The file information as returned by lstat on the file entry.
        :type finfo: lstat result
    """
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

def primitive_list_directory(ssh_client: paramiko.SSHClient, directory: str):
    """
        Uses a primitive method to create a list of the files and folders in a directory
        by running the 'ls -al' commands on the directory.  This is required if the SSH
        server does not support sftp.

        :param ssh_client: A :class:`paramiko.SSHClient` object that has already been connected
                           to the remote server.
        :type ssh_client: :class:`paramiko.SSHClient`
        :param directory: The remote directory to get a list catalog for.
        :type directory: str 
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

def primitive_list_tree(ssh_client: paramiko.SSHClient, treeroot: str, max_depth: int=1):
    """
        Uses a primitive method to create an information tree about the files and folders
        in a directory tree by running 'ls -al' commands on the directory tree.  This is
        required if the SSH server does not support sftp.

        :param ssh_client: A :class:`paramiko.SSHClient` object that has already been connected
                           to the remote server.
        :type ssh_client: :class:`paramiko.SSHClient`
        :param treeroot: The remote root directory to get a directory tree catalog for.
        :type treeroot: str
        :param max_depth: The maximum descent depth to go to when building the tree catalog.
        :type max_depth: int 
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

def primitive_list_tree_recurse(ssh_client: paramiko.SSHClient, rootdir: str, remaining: int):

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

def primitive_parse_directory_listing(dir:str, content: str):
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

def primitive_pull_file(ssh_client: paramiko.SSHClient, remotepath: str, localpath: str):

    copycmd = "cat %s" % remotepath

    status, stdout, stderr = ssh_execute_command(ssh_client, copycmd)

    if status != 0:
        raise Exception("Error pulling file using command. cmd=%s" % copycmd)

    with open(localpath, 'w') as lfile:
        lfile.write(stdout)

    return

def primitive_push_file(ssh_client: paramiko.SSHClient, localpath: str, remotepath: str):
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

def sftp_list_tree(sftp: paramiko.SFTPClient, treeroot: str, userlookup: Callable[[int, Optional[bool]], str], grouplookup: Callable[[int, Optional[bool]], str], max_depth: int=1):

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

def sftp_list_tree_recurse(sftp: paramiko.SFTPClient, rootdir: str, userlookup: Callable[[int, Optional[bool]], str], grouplookup: Callable[[int, Optional[bool]], str], remaining: int):

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

def ssh_execute_command(ssh_client: paramiko.SSHClient, command: str, pty_params=None, inactivity_timeout: float=DEFAULT_SSH_TIMEOUT, inactivity_interval: float=DEFAULT_SSH_RETRY_INTERVAL, chunk_size: int=1024, attach_pty: bool=False):
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

    if pty_params is not None:
        channel.get_pty(**pty_params)

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

class SshBase:

    def __init__(self, host: str, username: str, password: Optional[str] = None, keyfile: Optional[str] = None, keypasswd: Optional[str] = None,
                 allow_agent: bool = False, users: Optional[dict] = None, port: int = 22, primitive: bool = False, pty_params: Optional[dict] = None,
                 aspects=DEFAULT_ASPECTS):

        self._host = host
        
        self._username = username
        self._password = password
        self._keyfile = keyfile
        self._keypasswd = keypasswd
        self._allow_agent = allow_agent
        self._users = users
        self._port = port
        self._primitive = primitive
        self._pty_params = pty_params
        self._aspects = aspects

        self._ipaddr = socket.gethostbyname(self._host)

        self._user_lookup_table = {}
        self._group_lookup_table = {}

        if self._password is None and self._keyfile is None and not allow_agent:
            raise AKitInvalidConfigError("SshAgent requires either a 'password', an identity 'keyfile' or allow_agent=True be specified.")
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
    def pty_params(self):
        return self._pty_params

    @property
    def username(self):
        return self._username

    @property
    def users(self):
        return self._users

    def lookup_user_by_uid(self, uid: int, update=False):
        username = None

        if uid in self._user_lookup_table:
            username = self._user_lookup_table[uid]
        else:
            status, stdout, _ = self.run_cmd("id -n -u %d" % uid)
            if status == 0:
                username = stdout.strip()
                self._user_lookup_table[uid] = username

        return username

    def lookup_group_by_uid(self, gid: int, update=False):
        grpname = None

        if gid in self._group_lookup_table:
            grpname = self._group_lookup_table[gid]
        else:
            status, stdout, _ = self.run_cmd("id -n -g %d" % gid)
            if status == 0:
                grpname = stdout.strip()
                self._group_lookup_table[gid] = grpname

        return grpname

    def run_cmd(self, command: str, exp_status: Union[int, Sequence]=0, user: str = None, pty_params: dict = None, aspects: Optional[Aspects] = None):
        raise AKitNotOverloadedError("SshBase.run_cmd must be overloaded by derived class '%s'." % type(self).__name__)

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
            pkey = paramiko.pkey.PKey.from_private_key_file(self._keyfile, password=self._keypasswd)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(self._ipaddr, port=self._port, username=self._username, password=self._password, pkey=pkey)
        return ssh_client

    def _directory_tree(self, ssh_client, root_dir, depth=1):

        dir_info = {}

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

        return dir_info

    def _directory(self, ssh_client, root_dir):

        dir_info = {}

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

        return dir_info

    def _log_command_result(self, command, status, stdout, stderr, exp_status, logging_pattern):

        if type(exp_status) == int:
            if status == exp_status:
                if logging_pattern == LoggingPattern.ALL_RESULTS or logging_pattern == LoggingPattern.SUCCESS_ONLY:
                    logger.info(TEMPLATE_COMMAND_SUCCESS % (command, stdout, stderr) )
        else:
            if status in exp_status:
                if logging_pattern == LoggingPattern.ALL_RESULTS or logging_pattern == LoggingPattern.SUCCESS_ONLY:
                    logger.info(TEMPLATE_COMMAND_SUCCESS % (command, stdout, stderr))
            else:
                if logging_pattern == LoggingPattern.ALL_RESULTS or logging_pattern == LoggingPattern.FAILURE_ONLY:
                    logger.error(TEMPLATE_COMMAND_FAILURE % (command, stdout, stderr))
        return

    def _run_cmd(self, ssh_client, command: str, exp_status: Union[int, Sequence]=0, user: str = None, pty_params: dict = None, aspects: Optional[Aspects] = None):

        # Go through the overrides and if they are not passed use the agent defaults.
        if pty_params is None:
            pty_params = self._pty_params

        if aspects is None:
            aspects = self._aspects

        if user is not None:
            if self._users is None:
                errmsg = "In order to pass a 'user' parameter, you must create the SSHAgent with a 'users' parameter with a dictionary of user credentials."
                raise AKitInvalidConfigError(errmsg)
            if user not in self._users:
                errmsg = "The specified 'user=%s' was not found in the users credentials provided to SSHAgent."

        completion_timeout = aspects.completion_timeout
        completion_interval = aspects.completion_interval
        inactivity_timeout = aspects.inactivity_timeout
        inactivity_interval = aspects.inactivity_interval
        monitor_delay = aspects.monitor_delay
        logging_pattern = aspects.logging_pattern

        status, stdout, stderr = None, None, None

        this_thr = threading.current_thread()
        monmsg= "Thread failed to exit monitored scope. thid=%s thname=%s cmd=%s" % (this_thr.ident, this_thr.name, command)

        # Run the command using the SINGLE_RUN pattern, we run it once and then return the result
        if aspects.run_pattern == RunPattern.SINGLE_RUN:

                # Setup a monitored scope for the call to the remote device in case of timeout failure
                with MonitoredScope("RUNCMD-SINGLE_RUN", monmsg, timeout=inactivity_timeout + monitor_delay) as ms:

                    status, stdout, stderr = ssh_execute_command(ssh_client, command, pty_params=pty_params,
                        inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)

                self._log_command_result(command, status, stdout, stderr, exp_status, logging_pattern)

        # RUN_UNTIL_SUCCESS, run the command until we get a successful expected result or a completion timeout has occured
        elif aspects.run_pattern == RunPattern.RUN_UNTIL_SUCCESS:

            start_time = time.time()
            end_time = start_time + completion_timeout

            while True:

                # Setup a monitored scope for the call to the remote device in case of timeout failure
                with MonitoredScope("RUNCMD-RUN_UNTIL_SUCCESS", monmsg, timeout=inactivity_timeout + monitor_delay) as ms:
                    status, stdout, stderr = ssh_execute_command(ssh_client, command, pty_params=pty_params, 
                        inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)

                self._log_command_result(command, status, stdout, stderr, exp_status, logging_pattern)

                if type(exp_status) == int:
                    if status == exp_status:
                        break
                elif status in exp_status:
                    break

        # RUN_WHILE_SUCCESS, run the command while it is succeeds or a completion timeout has occured
        elif aspects.run_pattern == RunPattern.RUN_WHILE_SUCCESS:

            start_time = time.time()
            end_time = start_time + completion_timeout

            while True:

                with MonitoredScope("RUNCMD-RUN_WHILE_SUCCESS", monmsg, timeout=inactivity_timeout + monitor_delay) as ms:
                    status, stdout, stderr = ssh_execute_command(ssh_client, command, pty_params=pty_params,
                        inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)

                self._log_command_result(command, status, stdout, stderr, exp_status, logging_pattern)

                if type(exp_status) == int:
                    if status != exp_status:
                        break
                elif status not in exp_status:
                    break

        return status, stdout, stderr

    def _pull_file(self, ssh_client, remotepath, localpath):

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

        return

    def _push_file(self, ssh_client, localpath, remotepath):

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

        return


class SshSession(SshBase):
    def __init__(self, host: str, username: str, password: str=None, keyfile: Optional[str] = None, keypasswd: Optional[str] = None,
                 allow_agent: bool=False, users: Optional[dict] = None, port:int=22, primitive: bool = False, pty_params: Optional[dict] = None,
                 aspects: Aspects=DEFAULT_ASPECTS):
        SshBase.__init__(self, host, username, password=password, keyfile=keyfile, keypasswd=keypasswd, allow_agent=allow_agent, users=users,
                         port=port, primitive=primitive, pty_params=pty_params, aspects=aspects)

        self._ssh_client = None
        return

    def __enter__(self):
        self._ssh_client = self._create_client()
        return

    def __exit__(self, ex_val, ex_type, ex_tb):
        self._ssh_client.close()
        handled = False
        return handled

    def run_cmd(self, command: str, exp_status: Union[int, Sequence]=0, user: str = None, pty_params: dict = None, aspects: Optional[Aspects] = None):

        status, stdout, stderr = self._run_cmd(self._ssh_client, command, user=user, pty_params=pty_params, aspects=aspects)

        return status, stdout, stderr

    def directory_tree(self, root_dir, depth=1, ssh_client=None):

        dir_info = self._directory_tree(self._ssh_client, root_dir, depth=depth)

        return dir_info

    def directory(self, root_dir, ssh_client=None):

        dir_info = self._directory(self._ssh_client, root_dir)

        return dir_info

    def pull_file(self, remotepath, localpath, ssh_client=None):

        self._pull_file(self._ssh_client, remotepath, localpath)

        return

    def push_file(self, localpath, remotepath, ssh_client=None):

        self._push_file(self._ssh_client, localpath, remotepath)

        return


class SshAgent(SshBase, LandscapeDeviceExtension):

    def __init__(self, host: str, username: str, password: Optional[str] = None, keyfile: Optional[str] = None, keypasswd: Optional[str] = None,
                 allow_agent: bool = False, users: Optional[dict] = None, port: int = 22, primitive: bool = False, pty_params: Optional[dict] = None,
                 aspects=DEFAULT_ASPECTS):
        SshBase.__init__(self, host, username, password=password, keyfile=keyfile, keypasswd=keypasswd, allow_agent=allow_agent, users=users,
                         port=port, primitive=primitive, pty_params=pty_params, aspects=aspects)
        LandscapeDeviceExtension.__init__(self)
        return

    def initialize(self, coord_ref: weakref.ReferenceType, basedevice_ref: weakref.ReferenceType, extid: str, location: str, configinfo: dict):
        """
            Initializes the landscape device extension. It is not required to call this function in order to use an SSHAgent, it is used
            when an agent is attached to a LandscapeDevice as a device extension.

            :param coord_ref: A weak reference to the coordinator that is managing interactions through this
                              device extension.
            :type coord_ref: weakref.ReferenceType
            :param extid: A unique reference that can be used to identify this device via the coordinator even if its location changes.
            :type extid: str
            :param location: The location reference where this device can be found via the coordinator.
            :type location: str
            :param 
        """
        LandscapeDeviceExtension.initialize(self, coord_ref, basedevice_ref, extid, location, configinfo)
        return

    def run_cmd(self, command: str, exp_status: Union[int, Sequence]=0, user: str = None, pty_params: dict = None, aspects: Optional[Aspects] = None):

        cleanup_client = False

        status, stdout, stderr = None, None, None

        try:
            if ssh_client is None:
                # If we are not passed in a client to use, we create one
                # and then clean it up before returning
                ssh_client = self._create_client()
                cleanup_client = True

            status, stdout, stderr = self._run_cmd(ssh_client, command, exp_status=exp_status, user=user, pty_params=pty_params, aspects=aspects)

        finally:
            # If we created a client, clean it up
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

            dir_info = self._directory_tree(ssh_client, root_dir, depth=depth)

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

            dir_info = self._directory(ssh_client, root_dir)

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
            
            self._pull_file(ssh_client, remotepath, localpath)

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
            
            self._push_file(ssh_client, localpath, remotepath)

        finally:
            if cleanup_client:
                ssh_client.close()
                del ssh_client

        return
