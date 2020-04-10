
from flask_restplus import Namespace, Resource
from flask_restplus.reqparse import RequestParser

from akit.integration.landscaping import Landscape
from akit.integration.agents.upnpagent import UpnpAgent

landscape = Landscape()
upnp_agent = UpnpAgent()

DEVICES_NAMESPACE_PATH = "/devices"

devices_ns = Namespace("Devices v1", description="")

@devices_ns.route("/")
class AllDevicesCollection(Resource):

   def get(self):
        """
            Returns a list of devices
        """
        expected_upnp_devices = landscape.get_upnp_devices()

        found_upnp_devices = []

        for child in upnp_agent.children:
            cinfo = child.to_dict(brief=True)
            found_upnp_devices.append(cinfo)

        rtndata = {
            "status": "success",
            "expected": expected_upnp_devices,
            "found": found_upnp_devices
        }

        return rtndata

def publish_namespaces(version_prefix):
    ns_list = [
        (devices_ns, "".join([version_prefix, DEVICES_NAMESPACE_PATH]))
    ]
    return ns_list
