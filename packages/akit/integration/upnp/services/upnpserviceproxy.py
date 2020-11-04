
import requests
import traceback

from xml.etree.ElementTree import fromstring as xml_fromstring

from akit.integration.upnp.soap import SoapProcessor, SOAPError, SOAPProtocolError, SOAP_TIMEOUT
from akit.integration.upnp.upnperrors import UpnpError

class UpnpServiceProxy:
    """
    """

    SERVICE_ID = None
    SERVICE_TYPE = None

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

    def proxy_link_service_to_device(self, device_ref, service_description):

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

    def proxy_set_call_parameters(self, host, baseURL, controlURL, eventSubURL, serviceId=None, serviceType=None):

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

    def proxy_call_action(self, action_name: str, arguments: dict = {}, auth: dict = None, headers: dict = {} ):

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

    def proxy_get_variable_value(self, var_name):
        var_value = None

        action_name = "Get" + var_name

        resp_dict = self.proxy_call_action(action_name)

        return var_value

    def proxy_set_variable_value(self, var_name, var_value):

        action_name = "Set" + var_name

        resp_dict = self.proxy_call_action(action_name)

        return

    def subscribe_to_event(self, eventname, timeout=None):
        """
            Creates a subscription to the service events for this service.
        """
        device = self._device_ref()
        event_var = device.subscribe_to_event(self.SERVICE_TYPE, eventname, timeout=timeout)
        return event_var