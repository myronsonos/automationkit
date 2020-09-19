
import enum

class DnsLiftimePercent(enum.IntEnum):
    Expired = 100
    Stale = 50
    Refresh = 75

@enum.unique
class DnsEntryClass(enum.IntEnum):
    IN = 1
    CS = 2
    CH = 3
    HS = 4
    NONE = 254
    ANY = 255
    MASK = 0x7FFF
    UNIQUE = 0x8000

@enum.unique
class DnsEntryType(enum.IntEnum):
    A = 1
    NS = 2
    MD = 3
    MF = 4
    CNAME = 5
    SOA = 6
    MB = 7
    MG = 8
    MR = 9
    NULL = 10
    WKS = 11
    PTR = 12
    HINFO = 13
    MINFO = 14
    MX = 15
    TXT = 16
    AAAA = 28
    SRV = 33
    ANY = 255

class DnsFlags(enum.IntEnum):
    FLAGS_AA = 0x0400  # Authoritative answer
    FLAGS_TC = 0x0200  # Truncated
    FLAGS_RD = 0x0100  # Recursion desired
    FLAGS_RA = 0x8000  # Recursion available

    FLAGS_Z = 0x0040  # Zero
    FLAGS_AD = 0x0020  # Authentic data
    FLAGS_CD = 0x0010  # Checking disabled

class DnsResponseFlags(enum.IntEnum):
    FLAGS_QR_MASK = 0x8000  # query response mask
    FLAGS_QR_QUERY = 0x0000  # query
    FLAGS_QR_RESPONSE = 0x8000  # response

