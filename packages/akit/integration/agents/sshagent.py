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
import time

from akit.aspects import RunPattern, DEFAULT_ASPECTS

import paramiko

DEFAULT_SSH_TIMEOUT = 300
DEFAULT_SSH_RETRY_INTERVAL = 1

def execute_command(ssh_client, command, inactivity_timeout=DEFAULT_SSH_TIMEOUT, inactivity_interval=DEFAULT_SSH_RETRY_INTERVAL, chunk_size=1024):
    """

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
            time.sleep(inactivity_interval)

        now_time = time.time()
        if now_time > end_time:
            diff_time = now_time - start_time
            err_msg = "Timeout while executing SSH command.\n    command=%s\n    start=%r end=%r now=%r diff=%r" % (
                command, start_time, end_time, now_time, diff_time)
            raise TimeoutError(err_msg)

    stdout = stdout_buffer.decode()
    del stdout_buffer

    stderr = stderr_buffer.decode()
    del stderr_buffer

    return status, stdout, stderr

def list_directory(ssh_client, directory):
    return

def list_tree(ssh_client, treeroot, max_depth=1):
    return

def list_tree_recurse(ssh_client, rootdir, remaining):
    return

#                    PERMS          LINKS   OWNER       GROUPS    SIZE   MONTH  DAY  TIME    NAME
#                  rwxrwxrwx         24      myron      myron     4096   Jul    4   00:37  PCBs
REGEX_DIRECTORY_ENTRY = re.compile(r"([\S]+)[\s]+([0-9]+)[\s]+([\S]+)[\s]+([\S]+)[\s]+([0-9]+)[\s]+([A-za-z]+[\s]+[0-9]+[\s]+[0-9:]+)[\s]+([\S\s]+)")

def primitive_list_directory(ssh_client, directory):
    """
        Uses a primitive method to create a list of the files and folders in a directory
        by running the 'ls -al' commands on the directory.  This is required if the SSH
        server does not support sftp.
    """
    entries = None

    ls_cmd = "ls -al %s" % directory

    status, stdout, stderr = execute_command(ssh_client, ls_cmd)

    if status == 0:
        entries = primitive_parse_directory_listing(directory, stdout)
    else:
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


class SshSession:
    def __init__(self, host, username, password, port=22,aspects=DEFAULT_ASPECTS):
        self._host = host
        self._ipaddr = socket.gethostbyname(host)
        self._port = port
        self._username = username
        self._password = password
        self._aspects = aspects
        self._ssh_client = None
        self._primitive_mode = False
        return

    def __enter__(self):
        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_client.connect(self._ipaddr, port=self._port, username=self._username, password=self._password)
        return

    def __exit__(self, ex_val, ex_type, ex_tb):
        self._ssh_client.close()
        handled = True
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
            status, stdout, stderr = execute_command(self._ssh_client, command, inactivity_timeout=timeout, inactivity_interval=interval)

        elif aspects.run_pattern == RunPattern.RUN_UNTIL_SUCCESS:
            while True:
                status, stdout, stderr = execute_command(self._ssh_client, command, inactivity_timeout=timeout, inactivity_interval=interval)
                if status == 0:
                    break
                else:
                    pass

        elif aspects.run_pattern == RunPattern.RUN_WHILE_SUCCESS:
            while True:
                status, stdout, stderr = execute_command(self._ssh_client, command, inactivity_timeout=timeout, inactivity_interval=interval)
                if status != 0:
                    break
                else:
                    pass

        return status, stdout, stderr


class SshAgent:

    def __init__(self, host, username, password, port=22, primitive=None, aspects=DEFAULT_ASPECTS):
        self._host = host
        self._ipaddr = socket.gethostbyname(self._host)
        self._port = port
        self._username = username
        self._password = password
        self._aspects = aspects
        if primitive is None:
            self._primitive = True
        self._primitive = primitive
        return

    @property
    def aspects(self):
        return self._aspects

    @property
    def host(self):
        return self._host

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
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(self._ipaddr, port=self._port, username=self._username, password=self._password)
                cleanup_client = True

            if aspects.run_pattern == RunPattern.SINGLE_RUN:
                status, stdout, stderr = execute_command(ssh_client, command, inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)

            elif aspects.run_pattern == RunPattern.RUN_UNTIL_SUCCESS:
                while True:
                    status, stdout, stderr = execute_command(ssh_client, command, inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)
                    if status == 0:
                        break
                    else:
                        pass

            elif aspects.run_pattern == RunPattern.RUN_WHILE_SUCCESS:
                while True:
                    status, stdout, stderr = execute_command(ssh_client, command, inactivity_timeout=inactivity_timeout, inactivity_interval=inactivity_interval)
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
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(self._ipaddr, port=self._port, username=self._username, password=self._password)
                cleanup_client = True

            if not self._primitive:
                transport = ssh_client.get_transport()
                try:

                    ftp = paramiko.SFTPClient.from_transport(transport)
                    try:
                        ftp.chdir(root_dir)
                        dir_entries = ftp.listdir()

                        for nitem in dir_entries:
                            print(nitem)
                    finally:
                        ftp.close()
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

if __name__ == "__main__":
    from pprint import pprint
    agent = SshAgent("192.168.1.40", username="myron", password="Skate4Fun##", primitive=True)

    dir_info = agent.directory_tree("/home", depth=3)

    pprint(dir_info, indent=4)
