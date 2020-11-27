
from enum import IntEnum
from typing import Any, Optional, Union, cast

from akit.integration.mdns.dnsconst import DnsEntryClass, DnsEntryType

class DnsEntry:
    """
        Represents a DNS entry.
    """
    def __init__(self, name: str, etype: 'DnsEntryType', eclass: 'DnsEntryClass') -> None:
        self.key = name.lower()
        self.name = name
        self.etype = etype
        self.eclass = (eclass & DnsEntryClass.MASK)
        self.unique = (eclass & DnsEntryClass.UNIQUE) != 0
        return

    def as_dns_string(self, hdr: str, other: Optional[Union[bytes, str]]) -> str:
        ostr = "%s[%s,%s" % (hdr, self.etype.name, self.eclass.name)

        if self.unique:
            ostr += "-unique,"
        else:
            ostr += ","

        ostr += self.name

        if other is not None:
            ostr += "]=%s" % cast(Any, other)
        else:
            ostr += "]"

        return ostr

    def __eq__(self, other: Any) -> bool:
        iseq = self.name == other.name and self.eclass == other.eclass and \
            self.etype == self.etype and isinstance(other, DnsEntry)
        return iseq

    def __ne__(self, other: Any) -> bool:
        neq = not self.__eq__(other)
        return neq
