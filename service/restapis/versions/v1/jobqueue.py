
from flask_restplus import Namespace, Resource
from flask_restplus.reqparse import RequestParser

from akit.integration.agents.upnpagent import UpnpAgent
from akit.integration.landscaping import Landscape

landscape = Landscape()
upnp_agent = UpnpAgent()

JOBQUEUE_NAMESPACE_PATH = "/jobqueue"

jobqueue_ns = Namespace("Job Queue v1", description="APIs for information about the pending jobs.")

@jobqueue_ns.route("/")
class JobQueueSummary(Resource):

   def get(self):
        """
            Returns a job queue summary
        """

        rtndata = {
            "status": "success",
            "jobs": {
                "current": {
                    "title": "Automation Test Run",
                    "runid": "21ec13f0-f948-4b3e-be55-9341276c93ad",
                    "branch": None,
                    "build": None,
                    "flavor": None,
                    "start": "2020-02-29 19:47:09.180623",
                    "stop": "2020-02-29 19:47:09.216462",
                    "progress": .5,
                    "result": "FAILED",
                    "landscape": None,
                    "detail": {
                        "errors": 0,
                        "failed": 1,
                        "skipped": 0,
                        "passed": 3,
                        "total": 4
                    }
                },
                "queue": [
                    {
                        "title": "Automation Test Run",
                        "branch": None,
                        "build": None,
                        "flavor": None,
                        "added": "2020-04-09 20:34:09.216462",
                        "parameters": {}
                    }
                ]
            }
        }

        return rtndata

def publish_namespaces(version_prefix):
    ns_list = [
        (jobqueue_ns, "".join([version_prefix, JOBQUEUE_NAMESPACE_PATH]))
    ]
    return ns_list
