
from flask_restplus import Namespace, Resource
from flask_restplus.reqparse import RequestParser

from akit.integration.agents.upnpagent import UpnpAgent
from akit.integration.landscaping import Landscape

landscape = Landscape()
upnp_agent = UpnpAgent()

RESULTS_NAMESPACE_PATH = "/results"

results_ns = Namespace("Results v1", description="APIs for information about results.")

@results_ns.route("/")
class ResultsSummary(Resource):

   def get(self):
        """
            Returns a job queue summary
        """
        expected_upnp_devices = landscape.get_upnp_devices()

        found_upnp_devices = []

        for child in upnp_agent.children:
            cinfo = child.to_dict(brief=True)
            found_upnp_devices.append(cinfo)

        rtndata = {
            "status": "success",
            "jobs": {
                "current": {
                    "job": "Grouping and Ungrouping",
                    "progress": .5
                },
                "prev": {
                    "job": "Playback",
                    "progress": 1.0,
                    "results": ""
                }
            },
            "landscape":{
                "pod": {
                    "expected": expected_upnp_devices,
                    "found": found_upnp_devices
                }
            }
        }

        return rtndata

def publish_namespaces(version_prefix):
    ns_list = [
        (results_ns, "".join([version_prefix, RESULTS_NAMESPACE_PATH]))
    ]
    return ns_list
