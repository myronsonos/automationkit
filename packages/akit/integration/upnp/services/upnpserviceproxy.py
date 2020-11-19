"""
.. module:: upnpserviceproxy
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpServiceProxy` class which is the base class
               all services proxied.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import requests
import threading
import traceback

from xml.etree.ElementTree import fromstring as xml_fromstring

from akit.xlogging.foundations import getAutomatonKitLogger

from akit.integration.upnp.soap import SoapProcessor, SOAPError, SOAPProtocolError, SOAP_TIMEOUT
from akit.integration.upnp.upnperrors import UpnpError
from akit.integration.upnp.services.upnpeventvar import UpnpEventVar

logger = getAutomatonKitLogger()

class UpnpServiceProxy:
    """
    """

    SERVICE_ID = None
    SERVICE_TYPE = None

    SERVICE_EVENT_VARIABLES = {}

    def __init__(self):
        self._device_ref = None
        self._soap_processor = SoapProcessor()

        self._host = None
        self._baseURL = None

        self._controlURL = None
        self._eventSubURL = None
        self._SCPDURL = None
        self._serviceType = None

        self._serviceId = None

        self._validate_parameter_values = True

        self._service_lock = threading.RLock()
        self._variables = {}
        self._subscription_id = None
        self._subscription_expiration = None

        self._create_event_variables_from_list()
        return

    @property
    def baseUrl(self):
        return self._baseURL

    @property
    def controlURL(self):
        return self._controlURL

    @property
    def device(self):
        return self._device_ref()

    @property
    def eventSubURL(self):
        return self._eventSubURL

    @property
    def host(self):
        return self._host

    @property
    def SCPDURL(self):
        return self._SCPDURL

    @property
    def serviceId(self):
        return self._serviceId

    @property
    def serviceType(self):
        return self._serviceType

    def lookup_event_variable(self, eventname):
        """
            Creates a subscription to the service events for this service.
        """
        varobj = None

        varkey = "{}/{}".format(self.SERVICE_TYPE, eventname)

        self._service_lock.acquire()
        try:
            varobj = self._variables[varkey]
        finally:
            self._service_lock.release()

        return varobj

    def subscribe_to_events(self, timeout=None):
        """
            Creates a subscription to the service events for this service.
        """
        success = False

        device = self._device_ref()
        sid, expiration = device.subscribe_to_events(self, timeout=timeout)

        if sid is not None:
            success = True
            self._service_lock.acquire()
            try:
                self._subscription_id = sid
                self._subscription_expiration = expiration
            finally:
                self._service_lock.release()

        return success

    def yield_service_lock(self):
        self._service_lock.acquire()
        try:
            yield
        finally:
            self._service_lock.release()

    def _create_event_variable(self, event_name, data_type=None, default=None, allowed_list=None):

        variable_key = "{}/{}".format(self.SERVICE_TYPE, event_name)
        event_var = UpnpEventVar(variable_key, event_name, self, data_type=data_type, default=default, allowed_list=allowed_list)
        self._variables[variable_key] = event_var
        return


    def _create_event_variables_from_list(self):

        for event_name in self.SERVICE_EVENT_VARIABLES:
            event_info = self.SERVICE_EVENT_VARIABLES[event_name]
            self._create_event_variable(event_name, **event_info)

        return

    def _proxy_link_service_to_device(self, device_ref, service_description):

        device = device_ref()

        self._device_ref = device_ref

        self._host = device.host
        self._baseURL = device.URLBase

        self._controlURL = service_description.controlURL
        self._eventSubURL = service_description.eventSubURL
        self._SCPDURL = service_description.SCPDURL
        self._serviceId = service_description.serviceId
        self._serviceType = service_description.serviceType

        return

    def _proxy_set_call_parameters(self, host, baseURL, controlURL, eventSubURL, serviceId=None, serviceType=None):

        self._host = host

        if serviceId is None:
            serviceId = self.SERVICE_ID

        if serviceType is None:
            serviceType = self.SERVICE_TYPE

        self._baseURL = baseURL

        self._controlURL = controlURL
        self._eventSubURL = eventSubURL
        self._serviceId = serviceId
        self._serviceType = serviceType
        return

    def _proxy_call_action(self, action_name: str, arguments: dict = {}, auth: dict = None, headers: dict = {} ):

        call_url = self.controlURL
        if self._baseURL is not None:
            call_url = self._baseURL + call_url

        call_body = self._soap_processor.create_request(action_name, arguments, typed=self.serviceType)

        call_headers = {
            'SOAPAction': '"%s#%s"' % (self.serviceType, action_name),
            'Host': self._host,
            'Content-Type': 'text/xml',
            'Content-Length': str(len(call_body)),
        }
        call_headers.update(headers)

        resp = None
        try:
            resp = requests.post(
                call_url,
                call_body,
                headers=call_headers,
                timeout=SOAP_TIMEOUT,
                auth=auth
            )
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            if resp is not None:
                # If the body of the error response contains XML then it should be a UPnP error,
                # extract the UPnP error information and raise a UpnpError
                content_type = resp.headers["CONTENT-TYPE"]
                if content_type.find('text/xml') == -1:
                    raise
        except:
            errmsg = traceback.format_exc()
            print(errmsg)
            raise

        resp_content = resp.content.strip()

        resp_dict = None
        status_code = resp.status_code
        if status_code >= 200 and status_code < 300:
            resp_dict = self._soap_processor.parse_response(action_name, resp_content, typed=self.serviceType)
        else:
            errorCode, errorDescription = self._soap_processor.parse_response_error_for_upnp(action_name, resp_content, status_code, typed=self.serviceType)
            raise UpnpError(errorCode, errorDescription, "host=%s action=%s args=%s" % (self._host, action_name, repr(arguments)))

        return resp_dict

    def _proxy_get_variable_value(self, var_name):
        var_value = None

        action_name = "Get" + var_name

        resp_dict = self.proxy_call_action(action_name)

        return var_value

    def _proxy_set_variable_value(self, var_name, var_value):

        action_name = "Set" + var_name

        resp_dict = self.proxy_call_action(action_name)

        return

    def _update_event_variables(self, propertyNodeList):

        self._service_lock.acquire()
        try:
            for propNodeOuter in propertyNodeList:
                # Get the first node of the outer property node
                propNode = propNodeOuter.getchildren()[0]

                event_name = propNode.tag
                event_value = propNode.text

                var_key = "{}/{}".format(self.SERVICE_TYPE, event_name)

                if var_key in self._variables:
                    varobj = self._variables[var_key]
                    varobj.sync_update(event_value, service_locked=True)
                else:
                    self._service_lock.release()
                    try:
                        host = self._device_ref().host
                        logger.error("UpnpServiceProxy: Received value for unknown host=%s vkey=%s event=%s value=%r" % (host, var_key, event_name, event_value))
                    finally:
                        self._service_lock.acquire()
        finally:
            self._service_lock.release()

        return
