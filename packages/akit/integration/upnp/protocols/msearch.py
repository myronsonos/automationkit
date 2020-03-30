
import ssdp
import weakref

class MSearchTargets:
    ROOTDEVICE = "upnp:rootdevice"
    ALL="ssdp:all"

class MSearchKeys:
    CACHE_CONTROL = "CACHE-CONTROL"
    EXT = "EXT"
    LOCATION = "LOCATION"
    SERVER = "SERVER"
    ST = "ST"
    USN = "USN"


class MSearchRootDeviceProtocol(ssdp.SimpleServiceDiscoveryProtocol):
    PORT = 1900
    HEADERS = {
        "ST": MSearchTargets.ROOTDEVICE,
        "Man": "ssdp:discover",
        "MX": "1"
    }

    def __init__(self, agent):
        self._agent_ref = weakref.ref(agent)
        return

    def response_received(self, response, addr):
        print(response, addr)
        print()

        reason = response.reason
        status_code = response.status_code
        version = response.version
        headers = dict(response.headers)

        # Process the packet
        location = headers[MSearchKeys.LOCATION]

        # promote our reference to the agent and push and update
        agent = self._agent_ref()
        if agent is not None:
            agent._update_root_device(location, headers)

        return

    def request_received(self, request, addr):
        print(request, addr)
        print()
        return