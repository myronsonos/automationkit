
from akit.integration.mdns.dnsentry import DnsEntry, DnsEntryType

class DnsQuestion(DnsEntry):
    """
        A DNS question entry.
    """
    def __init__(self, name: str, etype: 'DnsEntryType', eclass: 'DnsEntryClass') -> None:
        super(DnsQuestion, self).__init__(name, etype, eclass)
        return

    def answered_by(self, rec: 'DnsRecord') -> bool:
        """
            Returns true if the question is answered by the record.
        """
        bval = self.eclass == rec.eclass and \
            (self.etype == rec.etype or self.etype == DnsEntryType.ANY) and \
            self.name == rec.name
        return bval

    def as_dns_string(self) -> str:
        """
            String representation
        """
        rval = super(DnsQuestion, self).as_dns_string("question", None)
        return rval