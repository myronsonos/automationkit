
import requests
import traceback



from akit.integration.upnp.soap import SoapProcessor, SOAPError, SOAPProtocolError, SOAP_TIMEOUT

class UpnpServiceProxy:
    """
    """

    SERVICE_ID = None
    SERVICE_TYPE = None

    def __init__(self):
        self._host = None
        self._baseURL = None
        self._description = None
        self._soap_processor = SoapProcessor()

        self._controlURL = None
        self._eventSubURL = None
        self._SCPDURL = None
        self._serviceId = None
        self._serviceType = None

        self._validate_parameter_values = True
        return

    @property
    def baseUrl(self):
        return self._baseURL

    @property
    def controlURL(self):
        return self._controlURL

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

    def proxy_update_description(self, host, baseURL, description):
        self._host = host
        self._baseURL = baseURL
        self._description = description

        self._controlURL = self._description.controlURL
        self._eventSubURL = self._description.eventSubURL
        self._SCPDURL = self._description.SCPDURL
        self._serviceId = self._description.serviceId
        self._serviceType = self._description.serviceType

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
            # If the body of the error response contains XML then it should be a UPnP error,
            # otherwise reraise the HTTPError.
            errmsg = traceback.format_exc()
            print(errmsg)
            raise

        resp_content = resp.content.strip()

        resp_dict = self._soap_processor.parse_response(action_name, resp_content, typed=self.serviceType)

        return resp_dict

    def proxy_get_variable_value(self, var_name):
        var_value = None

        return var_value

    def proxy_set_variable_value(self, var_name, var_value):

        return