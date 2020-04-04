
import socket
import fcntl
import struct

from akit.compat import bytes_cast


def get_ip_address(ifname):
    ifname = bytes_cast(ifname)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sfd = s.fileno()
    ifname_packed = struct.pack('256s', ifname[:15])
    iface = socket.inet_ntoa(
        fcntl.ioctl(sfd,
        0x8915,  # SIOCGIFADDR
        ifname_packed)[20:24])
    return iface
