
import os
import sys

from argparse import ArgumentParser

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring as xml_fromstring

DIR_UPNP_GENERATOR = os.path.dirname(__file__)

DIR_UPNP_GENERATOR_DYNAMIC_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "dynamic", "services")
DIR_UPNP_GENERATOR_STANDARD_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "standard", "services")

UPNP_SERVICE_NAMESPACE = "urn:schemas-upnp-org:service-1-0"

MANUFACTURER_TO_BASE_CLASSES = {
    'SonosInc': ("akit.integration.upnp.devices.embedded.upnpdevice", "SonosDevice")
}

def process_action_list(svcActionListNode, namespaces=None):

    actionsTable = {}

    actionNodeList = svcActionListNode.findall("action", namespaces=namespaces)
    for actionNode in actionNodeList:
        action_name = actionNode.find("name", namespaces=namespaces).text
        argument_table = {}

        argumentListNode = actionNode.find("argumentList", namespaces=namespaces)
        if argumentListNode is not None:
            argumentNodeList = argumentListNode.findall("argument")
            for argumentNode in argumentNodeList:
                arg_info = {}
                arg_name = argumentNode.find("name", namespaces=namespaces).text
                arg_direction = argumentNode.find("direction", namespaces=namespaces).text

                arg_related = None
                argRelatedNode = argumentNode.find("relatedStateVariable", namespaces=namespaces)
                if argRelatedNode is not None:
                    arg_related = argRelatedNode.text

                arg_info["name"] = arg_name
                arg_info["direction"] = arg_direction
                arg_info["relatedStateVariable"] = arg_related
                argument_table[arg_name] = arg_info

        actionsTable[action_name] = { "name": action_name, "arguments": argument_table }

    return actionsTable

def process_service_state_table(svcStateTableNode, namespaces=None):

    variablesTable = {}
    typesTable = {}
    eventsTable = {}

    stateVariableNodeList = svcStateTableNode.findall("stateVariable", namespaces=namespaces)

    for stateVariableNode in stateVariableNodeList:

        variable_info = {}

        var_name = stateVariableNode.find("name", namespaces=namespaces).text
        variable_info["name"] = var_name

        send_events = "no"
        if "sendEvents" in stateVariableNode.attrib:
            send_events = stateVariableNode.attrib["sendEvents"].lower()
        else:
            sendEventsNode = stateVariableNode.find("sendEventsAttribute")
            if sendEventsNode is not None:
                send_events = sendEventsNode.text.lower()

        variable_info["sendEvents"] = send_events


        var_type = stateVariableNode.find("dataType", namespaces=namespaces).text
        variable_info["dataType"] = var_type

        allowedValueListNode = stateVariableNode.find("allowedValueList", namespaces=namespaces)
        if allowedValueListNode is not None:
            allowed_value_list = []
            for allowedValueNode in allowedValueListNode.findall("allowedValue", namespaces=namespaces):
                allowed_value = allowedValueNode.text
                allowed_value_list.append(allowed_value)
            variable_info["allowedValueList"] = allowed_value_list

        defaultValueNode = stateVariableNode.find("defaultValue", namespaces=namespaces)
        if defaultValueNode is not None:
            default_value = defaultValueNode.text
            variable_info["defaultValue"] = default_value

        if var_name.startswith("A_ARG_TYPE_"):
            typesTable[var_name] = variable_info
        else:
            variablesTable[var_name] = variable_info
            if send_events == "yes":
                eventsTable[var_name] = variable_info

    return variablesTable, typesTable, eventsTable


def generate_service_proxies(svc_desc_directory):

    for dirpath, dirnames, filenames in os.walk(svc_desc_directory, topdown=True):
        for nxtfile in filenames:
            serviceType, nxtfile_ext = os.path.splitext(nxtfile)

            svc_content = None

            fullpath = os.path.join(dirpath, nxtfile)
            with open(fullpath, 'r') as xf:
                svc_content = xf.read()

            docNode = xml_fromstring(svc_content)
            if docNode != None:

                namespaces = None
                doc_node_tag = docNode.tag
                if doc_node_tag.find("}") > 0:
                    default_ns = doc_node_tag[doc_node_tag.find("{"):doc_node_tag.find("}")]
                    namespaces = {"": default_ns}

                variablesTable = {}
                typesTable = {}
                eventsTable = {}

                svcStateTableNode = docNode.find("serviceStateTable", namespaces=namespaces)
                if svcStateTableNode is not None:
                    variablesTable, typesTable, eventsTable = process_service_state_table(svcStateTableNode, namespaces=namespaces)

                actionsTable = {}
                actionListNode = docNode.find("actionList", namespaces=namespaces)
                if actionListNode is not None:
                    actionsTable = process_action_list(actionListNode, namespaces=namespaces)

            else:
                errmsg = "WARNING: No serice node found in file:\n    %s\n" % fullpath
                print(errmsg, file=sys.stderr)

    return

def soapgenerator_main():
    parse = ArgumentParser()

    #if os.path.exists(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES):
    #    generate_service_proxies(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES)

    if os.path.exists(DIR_UPNP_GENERATOR_STANDARD_SERVICES):
        generate_service_proxies(DIR_UPNP_GENERATOR_STANDARD_SERVICES)

    return

if __name__ == "__main__":
    soapgenerator_main()
