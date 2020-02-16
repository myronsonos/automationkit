
import time

from akit.aspects import RunPattern, DEFAULT_ASPECTS

from paramiko import SSHClient

DEFAULT_SSH_TIMEOUT = 300
DEFAULT_RETRY_INTERVAL = 1

def execute_command(ssh_client, command, inactivity_timeout=DEFAULT_SSH_TIMEOUT, inactivity_interval=DEFAULT_RETRY_INTERVAL, chunk_size=1024):
    """

    """
    status = None
    stdout_buffer = bytearray()
    stderr_buffer = bytearray()

    start_time = time.time()
    end_time = start_time + inactivity_timeout

    channel = ssh_client.get_transport().open_session(timeout=inactivity_timeout)
    channel.exec_command(cmd)

    while True:
        # Grab exit status ready before checking to see if stdout_ready or stderr_ready are True
        exit_status_ready = channel.exit_status_ready()
        stdout_ready = channel.recv_ready()
        stderr_ready = channel.recv_stderr_ready()

        # If stdout_ready or stderr_ready are true, we read this round
        if stdout_ready or stderr_ready:
            if stdout_ready:
                rcv_data = channel.recv(chunk_size)
                stdout_buffer.append(rcv_data)
            if stderr_ready:
                rcv_data = bychannel.recv_stderr(chunk_size)
                stderr_buffer.append(rcv_data)

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


class SshSession:
    def __init__(self, username, password, aspects=None):
        self._username = username
        self._password = password
        self._aspects = aspects
        self._ssh_client = None
        return

    def __enter__(self):
        self._ssh_client = SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_client.connect(self._host, self._port, username, None, key)
        return

    def __exit__(self, ex_val, ex_type, ex_tb):
        self._ssh_client.close()
        handled = True
        return handled

    def run_cmd(self, command, aspects=None):

        if aspects is None:
            aspects = self._aspects

        timeout=aspects.timeout
        interval=aspects.interval

        status = None
        stdout = None
        stderr = None

        if aspects.run_pattern == RunPattern.SINGLE_RUN:
            status, stdout, stderr = execute_command(self._ssh_client, command, timeout=timeout, interval=interval)

        elif aspects.run_pattern == RunPattern.RUN_UNTIL_SUCCESS:
            while True:
                status, stdout, stderr = execute_command(self._ssh_client, command, timeout=timeout, interval=interval)
                if status == 0:
                    break
                else:
                    pass

        elif aspects.run_pattern == RunPattern.RUN_WHILE_SUCCESS:
            while True:
                status, stdout, stderr = execute_command(self._ssh_client, command, timeout=timeout, interval=interval)
                if status != 0:
                    break
                else:
                    pass

        return status, stdout, stderr


class SshAgent:

    def __init__(self, host, username, password, port=22, aspects=DEFAULT_RETRY_INTERVAL):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._aspects = aspects
        return

    def run_cmd(self, command, aspects=None, ssh_client=None):

        if aspects is None:
            aspects = self._aspects

        timeout=aspects.timeout
        interval=aspects.interval

        cleanup_client = False
        status = None
        stdout = None
        stderr = None
        try:
            if ssh_client is None:
                ssh_client = SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(self._host, self._port, username, None, key)
                cleanup_client = True

            if aspects.run_pattern == RunPattern.SINGLE_RUN:
                status, stdout, stderr = execute_command(ssh_client, command, timeout=timeout, interval=interval)

            elif aspects.run_pattern == RunPattern.RUN_UNTIL_SUCCESS:
                while True:
                    status, stdout, stderr = execute_command(ssh_client, command, timeout=timeout, interval=interval)
                    if status == 0:
                        break
                    else:
                        pass

            elif aspects.run_pattern == RunPattern.RUN_WHILE_SUCCESS:
                while True:
                    status, stdout, stderr = execute_command(ssh_client, command, timeout=timeout, interval=interval)
                    if status != 0:
                        break
                    else:
                        pass

        finally:
            if cleanup_client:
                ssh_client.close()
                del ssh_client

        return status, stdout, stderr

