
"""
.. module:: looperqueue
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains a :class:`LooperQueue` which provides a thread-safe queue for
        for the :class:`Looper` and :class:`LooperPool`.

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

import threading
import time

from akit.exceptions import AKitSemanticError

class ReadWriteLock:

    def __init__(self):
        self._read_gate = threading.Event()
        self._read_gate.set()
        self._write_gate = threading.Semaphore(1)
        self._read_write_pivot = 0
        self._lock = threading.Lock()

        self._readers = []
        self._writer = None
        self._writers_waiting = 0
        return

    def acquire_read(self, timeout=None):

        self._read_gate.wait()

        tid = threading.get_ident()
        start_time = time.time()

        try:
            self._lock.acquire()
            try:
                self._readers.append(tid)

                while True:
                    if self._read_write_pivot >= 0:
                        self._read_write_pivot += 1
                        break
                    else:
                        self._lock.release()
                        try:
                            time_left = time.time() - start_time
                            if time_left < 0:
                                raise TimeoutError("Timeout waiting on read lock.")

                            self._read_gate.wait(timeout=time_left)
                        finally:
                            self._lock.acquire()

            finally:
                self._lock.release()
        except TimeoutError:
            now_time = time.time()
            elapsed = now_time - start_time
            errmsg = "Timeout waiting to acquire read lock. start=%d end=%d elapesed=%d" % (start_time, now_time, elapsed)
            raise TimeoutError(errmsg)

        return

    def acquire_write(self, timeout=None):

        tid = threading.get_ident()
        start_time = time.time()

        # Block new readers from starting to read
        self._read_gate.clear()

        try:
            self._lock.acquire()
            self._writers_waiting += 1
            try:
                while self._read_write_pivot != 0:
                    self._lock.release()
                    try:

                        time_left = time.time() - start_time
                        if time_left < 0:
                            raise TimeoutError("Timeout waiting on write lock.")

                        self._write_gate.acquire(timeout=time_left)

                    finally:
                        self._lock.acquire()

                self._writers_waiting -= 1
                self._read_write_pivot = -1
                self._writer = tid
            finally:
                self._lock.release()
        except TimeoutError:
            now_time = time.time()
            elapsed = now_time - start_time
            errmsg = "Timeout waiting to acquire write lock. start=%d end=%d elapesed=%d" % (start_time, now_time, elapsed)
            raise TimeoutError(errmsg)

        return

    def release_read(self):

        tid = threading.get_ident()

        self._lock.acquire()
        try:
            if tid not in self._readers:
                raise AKitSemanticError("Thread id(%d) attempting to release read lock when it was not owned." % tid)

            if self._read_write_pivot <= 0:
                raise AKitSemanticError("Thread id(%d) is attempting to release the ReadWriteLock when it is in a write or neutral state." % tid)

            self._read_write_pivot -= 1

        finally:
            self._lock.release()

        return

    def release_write(self):

        tid = threading.get_ident()

        self._lock.acquire()
        try:
            if self._writer != tid:
                raise AKitSemanticError("Thread id(%d) attempting to release write lock when it was not owned." % tid)

            if self._read_write_pivot >= 0:
                raise AKitSemanticError("Thread id(%d) is attempting to release the ReadWriteLock when it is in a read or neutral state." % tid)

            self._read_write_pivot += 1

            # Make the decision to allow readers before we let any waiting writers change
            # the count of self._writers_waiting
            if self._writers_waiting == 0:
                self._read_gate.set()

            # Don't release the write gate until we have checked to see if another writer is waiting
            self._write_gate.release()
        finally:
            self._lock.release()

        return