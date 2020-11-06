
import socket
import time

from enum import IntEnum
from typing import Any, Optional, Union, cast

from akit.exceptions import AKitAbstractMethodError

from akit.networking.interfaces import is_ipv6_address
from akit.integration.mdns.dnsconst import DnsEntryClass, DnsEntryType, DnsLiftimePercent
from akit.integration.mdns.dnsentry import DnsEntry

from akit.xtime import current_time_millis


class DnsRecord(DnsEntry):
    """
        A DNS record is a DNS entry that has a Time To Live or TTL attached.
    """
    def __init__(self, name: str, etype: 'DnsEntryType', eclass: 'DnsEntryClass', ttl: Union[float, int]) -> None:
        super(DnsRecord, self).__init__(name, etype, eclass)
        self.ttl = ttl
        self.updated = current_time_millis()
        self._when_expires = self._compute_time_marker(DnsLiftimePercent.Expired)
        self._when_refresh = self._compute_time_marker(DnsLiftimePercent.Refresh)
        self._when_stale = self._compute_time_marker(DnsLiftimePercent.Stale)
        return

    def as_dns_string(self, other: Optional[Union[bytes, str]]) -> str:
        """
            Creates a DNS string representation of the DNS record.
        """
        remaining_ttl = int(self.get_remaining_ttl(current_time_millis()))
        other = "%s/%s,%s" % (self.ttl, remaining_ttl, cast(Any, other))
        dnsstr = DnsEntry.as_dns_string(self, "record", other)
        return dnsstr

    def get_remaining_ttl(self, now: float) -> float:
        """
            Gets the remaining time to live (TTL) in seconds.
        """
        rval = max(0, (self._when_expires - now) / 1000)
        return rval

    def is_expired(self, now: Optional[float]) -> bool:
        """
            Returns true if this record is expired.
        """
        if now is None:
            now = time.time()

        bval = self._when_expires <= now
        return bval

    def is_stale(self, now: Optional[float]) -> bool:
        """
            Returns true if this record is stale.
        """
        if now is None:
            now = time.time()

        bval = self._when_stale <= now
        return bval

    def suppressed_by(self, msg: 'DNSIncoming') -> bool:
        """
            Returns true if any answer in a message can suffice for the information held in this
            record.
        """
        rtn_val = False
        for record in msg.answers:
            if self.suppressed_by_answer(record):
                rtn_val = True
                break
        return rtn_val

    def suppressed_by_answer(self, other: 'DNSRecord') -> bool:
        """
            Returns true if another record has same name, type and class, and if its TTL is at least
            half of this record's.
        """
        rtnval = self == other and other.ttl > (self.ttl / 2)
        return rtnval

    def update_ttl(self, other: 'DnsRecord') -> None:
        """
            Updateds the time to live TTL from the specified record.
        """
        self.updated = other.updated
        self.ttl = other.ttl
        self._when_expires = self._compute_time_marker(DnsLiftimePercent.Expired)
        self._when_refresh = self._compute_time_marker(DnsLiftimePercent.Refresh)
        self._when_stale = self._compute_time_marker(DnsLiftimePercent.Stale)
        return

    def write(self, out: 'DNSOutgoing') -> None:
        """
            Abstract method
        """
        raise AKitAbstractMethodError

    def _compute_time_marker(self, percent: int) -> float:
        marker = self.updated + (percent * self.ttl * 10)
        return marker
    
    def __eq__(self, other: Any) -> bool:
        """
            Abstract method
        """
        raise AKitAbstractMethodError

    def __ne__(self, other: Any) -> bool:
        """
            Abstract method
        """
        raise AKitAbstractMethodError

class DnsAddress(DnsRecord):
    """
        A DNS address record
    """

    def __init__(self, name: str, etype: int, eclass: int, ttl: int, address: bytes) -> None:
        super(DnsAddress, self).__init__(name, etype, eclass, ttl)
        self.address = address
        return

    def write(self, out: 'DNSOutgoing') -> None:
        """
            Used in constructing an outgoing packet
        """
        out.write_string(self.address)
        return

    def __eq__(self, other: Any) -> bool:
        """
            Tests equality on address
        """
        return (
            isinstance(other, DnsAddress) and DnsEntry.__eq__(self, other) and self.address == other.address
        )

    def __ne__(self, other: Any) -> bool:
        """
            Non-equality test
        """
        return not self.__eq__(other)

    def as_dns_string(self) -> str:
        """
            DNS string representation of a DNS address record.
        """
        dnsstr = ""

        try:
            addr_type = socket.AF_INET6 if is_ipv6_address(self.address) else socket.AF_INET
            dnsstr = super(DnsAddress, self).as_dns_string(socket.inet_ntop(addr_type, self.address))
        except Exception:  # TODO stop catching all Exceptions
            addrstr = self.address.decode('utf-8')
            dnsstr = super(DnsAddress, self).as_dns_string(addrstr)

        return dnsstr