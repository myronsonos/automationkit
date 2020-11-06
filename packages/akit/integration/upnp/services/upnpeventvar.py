"""
.. module:: akit.integration.upnp.services.upnpeventvar
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

import time

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

    def __init__(self, key, name, subscription_lock, sid=None, timeout=None, value=None, timestamp=None):
        """
            Constructor for the :class:`UpnpEventVar` object.

            :param key: The key {service type}/{event name} for this event
            :type key: str
            :param name: The name of the event this variable is storing information on.
            :type name: str
            :param subscription_lock: The lock from the :class:`UpnpRootDevice` device that hosts the service this
                                      variable is referencing state on.
            :type subscription_lock: :class:`threading.RLock`
            :param sid: The subscription id or SID assigned to the subscription for this event variable.
            :type sid: str
            :param timeout: The timeout assigned to the subscription reference by this :class:`UpnpEventVar` object.
            :type timeout: float
            :param value: Optional initially reported value for the variable.  This is used when we have reports for
                          variables that we are not subscribed to.
            :type value: various (str, int, etc)
            :param timestamp: The timestamp of the creation of this variable.  If a timestamp is passed then a value
                              needs to also be passed.
            :type timestamp: datetime

        """
        self._key = key
        self._name = name
        self._value = value
        self._sid = None
        self._timeout = None
        self._subscription_lock = subscription_lock

        if self._value is not None and timestamp is None:
            timestamp  = datetime.now()

        self._created = timestamp
        self._modified = timestamp
        return

    @property
    def created(self):
        """
            When the event variabled value was set for the first time.
        """
        return self._created

    @property
    def expired(self):
        """
            When the event variabled subscription has expired.
        """
        #TODO: Implement expired
        return True

    @property
    def key(self):
        """
            The key {service type}/{event name} for this event.
        """
        return self._key

    @property
    def state(self):
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
    def modified(self):
        """
            A datetime object that indicates when the value was last modified.
        """
        return self._modified

    @property
    def name(self):
        """
            The name of the event this variable is storing information on.
        """
        return self._name

    @property
    def value(self):
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

    def update_subscription_details(self, sid, timeout):
        """
            Called to update the subscription information for this event variable.
        """

        self._subscription_lock.acquire()
        try:
            self._sid = sid
            self._timeout = timeout
        finally:
            self._subscription_lock.release()

        return

    def sync_read(self):
        """
            Performs a threadsafe read of the value, modified, and state members of a
            :class:`UpnpEventVar` instance.
        """
        value, modified, state = None, None, UpnpEventVarState.UnInitialized

        self._subscription_lock.acquire()
        try:
            modified = self._modified

            if modified == datetime.min:
                state = UpnpEventVarState.Stale
            elif modified is not None:
                state = UpnpEventVarState.Valid

            value = self._value
        finally:
            self._subscription_lock.release()

        return value, modified, state

    def sync_update(self, value, sid=None):
        """
            Peforms a threadsafe update of the value, modified and sid members of a
            :class:`UpnpEventVar` instance.
        """
        modified = datetime.now()
        self._subscription_lock.acquire()
        try:
            if sid != None:
                self._sid = sid
            self._value, self._modified = value, modified
        finally:
            self._subscription_lock.release()

        return

    def wait_for_update(self, pre_modify_timestamp, timeout=60, interval=2):
        """
            Takes a datetime timestamp that is taken before a modification is made that
            will cause a state variable update and waits for the modified timestamp of
            this :class:`UpnpEventVar` instance to set to a timestamp that comes after the
            pre modification timestamp.

            :param pre_modify_timestamp: A timestamp taken from datetime.now() prior to engaging in
                                         an activity that will result in a state variable change.
            :type pre_modify_timestamp: datetime
            :param timeout: The time in seconds to wait for the update to occur.
            :type timeout: float
            :param interval: The time interval in seconds to wait before attempting to retry and
                             check to see if the modified timestamp has changed.
            :type interval: float

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

    def wait_for_value(self, timeout=60, interval=2):
        """
            Waits for this :class:`UpnpEventVar` instance to contain a value.  It constains a
            value once the modified timestamp has been set.

            :param timeout: The time in seconds to wait for a value to be present.
            :type timeout: float
            :param interval: The time interval in seconds to wait before attempting to retry and
                             check to see if the modified timestamp has been set.
            :type interval: float
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
