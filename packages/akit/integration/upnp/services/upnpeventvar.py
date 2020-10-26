
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

        If you need to ensure that the relationship between the value and last_update
        members are in sync with each other, then a sync_read and sync_update
        API is provided to ensure this synchronization.
    """

    def __init__(self, key, name, subscription_lock, value=None, timestamp=None):
        self._key = key
        self._name = name
        self._value = value
        self._last_update = timestamp
        self._sid = None
        self._subscription_lock = subscription_lock
        return

    @property
    def key(self):
        return self._key

    @property
    def state(self):
        rtn_state = UpnpEventVarState.UnInitialized

        last_update = self._last_update
        if last_update == datetime.min:
            rtn_state = UpnpEventVarState.Stale
        elif last_update is not None:
            rtn_state = UpnpEventVarState.Valid

        return rtn_state

    @property
    def last_update(self):
        return self._last_update

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def notify_byebye(self):
        """
            Handles a byebye notification and sets the last_update property to
            None to indicate that this UpnpEventVar is stale and will not receive
            any further updates.
            
            NOTE: After the byebye has been received, the values of the variable
            can still be used but should be with the understanding that they are
            stale and should be used with caution.
        """
        self._last_update = None
        return

    def sync_read(self):
        value, last_update, state = None, None, UpnpEventVarState.UnInitialized

        self._subscription_lock.aquire()
        try:
            last_update = self._last_update

            if last_update == datetime.min:
                state = UpnpEventVarState.Stale
            elif last_update is not None:
                state = UpnpEventVarState.Valid

            value = self._value
        finally:
            self._subscription_lock.release()

        return value, last_update, state

    def sync_update(self, value, timestamp, sid=None):

        self._subscription_lock.aquire()
        try:
            if sid != None:
                self._sid = sid
            self._value, self._last_update = value, timestamp
        finally:
            self._subscription_lock.release()

        return
