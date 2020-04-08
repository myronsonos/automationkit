
from flask_restplus import Namespace, Resource
from flask_restplus.reqparse import RequestParser

from akit.integration.agents.upnpagent import UpnpAgent

upnp_agent = UpnpAgent()

DEVICES_NAMESPACE_PATH = "/devices"

devices_ns = Namespace("Devices v1", description="")

@devices_ns.route("/")
class AllDevicesCollection(Resource):

   def get(self):
        """
            Returns a list of devices
        """
        items = []

        for child in upnp_agent.children:
            cinfo = child.to_dict()
            items.append(cinfo)

        rtndata = {
            "status": "success",
            "items": items,
            "count": len(items)
        }

        return rtndata

def publish_namespaces(version_prefix):
    ns_list = [
        (devices_ns, "".join([version_prefix, DEVICES_NAMESPACE_PATH]))
    ]
    return ns_list
