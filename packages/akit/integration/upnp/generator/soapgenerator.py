
import os
import sys

from argparse import ArgumentParser

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring as xml_fromstring

DIR_UPNP_GENERATOR = os.path.dirname(__file__)

DIR_UPNP_GENERATOR_DYNAMIC_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "dynamic", "services")
DIR_UPNP_GENERATOR_STANDARD_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "standard", "services")

UPNP_SERVICE_NAMESPACE = urn:schemas-upnp-org:service-1-0

MANUFACTURER_TO_BASE_CLASSES = {
    'SonosInc': ("akit.integration.upnp.devices.embedded.upnpdevice", "SonosDevice")
}

def create_service_state_context(svcStateNode):
    return

def generate_service_proxies(svc_desc_directory):

    for dirpath, dirnames, filenames in os.walk(svc_desc_directory, topdown):
        for nxtfile in filenames:
            serviceType, nxtfile_ext = os.path.splitext(nxtfile)

            svc_content = None

            fullpath = os.path.dirname(dirpath, nxtfile)
            with open(fullpath, 'r') as xf:
                svc_content = xf.read()

            docNode = xml_fromstring(svc_content)
            if docNode != None:
                svcStateTableNode = docNode.find("serviceStateTable")
                svcStateContext = create_service_state_context(svcStateTableNode)

                actionListNode = docNode.find("actionList")

            else:
                errmsg = "WARNING: No serice node found in file:\n    %s\n" % fullpath
                print(errmsg, file=sys.stderr)

    return

def soapgenerator_main():
    parse = ArgumentParser()

    if os.path.exists(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES):
        generate_service_proxies(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES)

    if os.path.exists(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES):
        generate_service_proxies(DIR_UPNP_GENERATOR_STANDARD_SERVICES)

    return

if __name__ == "__main__":
    soapgenerator_main()
