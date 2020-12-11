"""
.. module:: upnpeventvar
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpEventVar` class which is used to maintain
               variable subscription values and associated metadata.

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

from typing import Any, Tuple

import time
import weakref

from enum import IntEnum
from datetime import datetime

class UpnpEventVarState(IntEnum):
    UnInitialized = 0
    Valid = 1
    Stale = 2

class UpnpEventVar:
    """
        The UpnpEvent object is utilized to handle the storage and propagation
        of Upnp event values and updates and timeouts.

        NOTE: The properties associated with this object do not lock the
        subscription lock because they rely on eventual consistency.  They will
        always contain a value that was good at one point in time and will be
        updated in the future to a value that will be good for a new point in time.

        The "key" and "name" properties never change from thier initial values and
        they are set in the constructor when the object is under the control of only
        a single thread.

        If you need to ensure that the relationship between the value and modified
        members are in sync with each other, then a sync_read and sync_update
        API is provided to ensure this synchronization.
    """

    def __init__(self, key: str, name: str, service: weakref.ReferenceType, value: Any = None, data_type: Optional[str] = None, default: Any = None,
                 allowed_list=None, timestamp: datetime = None):
        """
            Constructor for the :class:`UpnpEventVar` object.

            :param key: The key {service type}/{event name} for this event
            :param name: The name of the event this variable is storing information on.
            :param value: Optional initially reported value for the variable.  This is used when we have reports for
                          variables that we are not subscribed to.
            :param timestamp: The timestamp of the creation of this variable.  If a timestamp is passed then a value
                              needs to also be passed.

        """
        self._key = key
        self._name = name
        self._service_ref = weakref.ref(service)
        self._value = value
        self._data_type = data_type
        self._default = default
        self._allowed_list = allowed_list
        self._timestamp = None

        if self._value is not None and timestamp is None:
            self._timestamp  = datetime.now()

        if value is None and default is not None:
            self._value = default

        self._created = timestamp
        self._modified = timestamp
        return

    @property
    def created(self) -> datetime:
        """
            When the event variabled value was set for the first time.
        """
        return self._created

    @property
    def expired(self) -> datetime:
        """
            When the event variabled subscription has expired.
        """
        #TODO: Implement expired
        return True

    @property
    def key(self) -> str:
        """
            The key {service type}/{event name} for this event.
        """
        return self._key

    @property
    def state(self) -> UpnpEventVarState:
        """
            The state of this event variable, UnInitialized, Valid or Stale
        """
        rtn_state = UpnpEventVarState.UnInitialized

        modified = self._modified
        if modified == datetime.min:
            rtn_state = UpnpEventVarState.Stale
        elif modified is not None:
            rtn_state = UpnpEventVarState.Valid

        return rtn_state

    @property
    def modified(self) -> datetime:
        """
            A datetime object that indicates when the value was last modified.
        """
        return self._modified

    @property
    def name(self) -> str:
        """
            The name of the event this variable is storing information on.
        """
        return self._name

    @property
    def value(self) -> Any:
        """
            The last value reported for the event variable this instance is referencing.
        """
        return self._value

    def notify_byebye(self):
        """
            Handles a byebye notification and sets the modified property to
            None to indicate that this UpnpEventVar is stale and will not receive
            any further updates.

            NOTE: After the byebye has been received, the values of the variable
            can still be used but should be with the understanding that they are
            stale and should be used with caution.
        """
        self._modified = None
        return

    def sync_read(self) -> Tuple[Any, datetime, UpnpEventVarState]:
        """
            Performs a threadsafe read of the value, modified, and state members of a
            :class:`UpnpEventVar` instance.
        """
        value, modified, state = None, None, UpnpEventVarState.UnInitialized

        service = self._service_ref()
        for _ in service.yield_service_lock():
            modified = self._modified

            if modified == datetime.min:
                state = UpnpEventVarState.Stale
            elif modified is not None:
                state = UpnpEventVarState.Valid

            value = self._value

        return value, modified, state

    def sync_update(self, value: Any, sid: str = None, service_locked: bool = False):
        """
            Peforms a threadsafe update of the value, modified and sid members of a
            :class:`UpnpEventVar` instance.
        """
        modified = datetime.now()

        if service_locked:
            self._value, self._modified = value, modified
        else:
            service = self._service_ref()
            for _ in service.yield_service_lock():
                self._value, self._modified = value, modified

        return

    def wait_for_update(self, pre_modify_timestamp: datetime, timeout: float = 60, interval: float = 2) -> Any:
        """
            Takes a datetime timestamp that is taken before a modification is made that
            will cause a state variable update and waits for the modified timestamp of
            this :class:`UpnpEventVar` instance to set to a timestamp that comes after the
            pre modification timestamp.

            :param pre_modify_timestamp: A timestamp taken from datetime.now() prior to engaging in
                                         an activity that will result in a state variable change.
            :param timeout: The time in seconds to wait for the update to occur.
            :param interval: The time interval in seconds to wait before attempting to retry and
                             check to see if the modified timestamp has changed.

        """
        now_time = time.time()
        start_time = now_time
        end_time = start_time + timeout
        while True:
            if now_time > end_time:
                raise TimeoutError("Timeout waiting for event variable to update.")

            if self._modified > pre_modify_timestamp:
                break
            time.sleep(interval)
            now_time = time.time()

        return self._value

    def wait_for_value(self, timeout: float = 60, interval: float = 2) -> Any:
        """
            Waits for this :class:`UpnpEventVar` instance to contain a value.  It constains a
            value once the modified timestamp has been set.

            :param timeout: The time in seconds to wait for a value to be present.
            :param interval: The time interval in seconds to wait before attempting to retry and
                             check to see if the modified timestamp has been set.
        """
        now_time = time.time()
        start_time = now_time
        end_time = start_time + timeout
        while True:
            if now_time > end_time:
                raise TimeoutError("Timeout waiting for event variable to update.")

            if self._modified is not None:
                break
            time.sleep(interval)
            now_time = time.time()

        return self._value

    def __str__(self) -> str:
        rtnstr = "name={} value={}".format(self._name, self._value)
        return rtnstr