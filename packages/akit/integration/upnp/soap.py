

from xml.etree.ElementTree import Element, SubElement, QName
from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import register_namespace

from akit.compat import bytes_cast, str_cast
from akit.exceptions import AKitCommunicationsProtocolError

NS_SOAP_ENV = "http://schemas.xmlsoap.org/soap/envelope/"
NS_SOAP_ENC = "http://schemas.xmlsoap.org/soap/encoding/"
NS_XSI = "http://www.w3.org/1999/XMLSchema-instance"
NS_XSD = "http://www.w3.org/1999/XMLSchema"

URI_SOAP_ENCODING = "http://schemas.xmlsoap.org/soap/encoding/"

XML_DOCUMENT_DECLARATION = '<?xml version="1.0" encoding="utf-8"?>'

SOAP_TIMEOUT = 60

PYTHON_TO_SOAP_TYPE_MAP = {
    bytes: 'xsd:string',
    str: 'xsd:string',
    int: 'xsd:int',
    float: 'xsd:float',
    bool: 'xsd:boolean'
}

class SOAPError(AKitCommunicationsProtocolError):
    """
    """


class SOAPProtocolError(AKitCommunicationsProtocolError):
    """
    """

class SoapProcessor:

    def __init__(self, encoding=URI_SOAP_ENCODING, envelope_attrib=None, typed=None):
        self._encoding = encoding
        self._envelope_attrib = envelope_attrib
        self._typed = typed
        return

    def create_request(self, action_name: str, arguments: dict, encoding=None, envelope_attrib=None, typed=None):

        register_namespace('', None)

        if encoding is None:
            encoding = self._encoding
        if envelope_attrib is None:
            envelope_attrib = self._envelope_attrib
        if typed is None:
            typed = self._typed

        envelope = Element("s:Envelope")
        if envelope_attrib:
            for eakey, eaval in envelope_attrib:
                envelope.attrib.update({eakey: eaval})
        else:
            envelope.attrib.update({'xmlns:s': NS_SOAP_ENV})
            envelope.attrib.update({'s:encodingStyle': encoding})

        body = SubElement(envelope, "s:Body")

        if typed:
            methElement = SubElement(body, "u:" + action_name)
            methElement.attrib.update({'xmlns:u': typed})
        else:
            methElement = SubElement(body, action_name)

        if arguments:
            for arg_name, arg_val in arguments.items():
                py_type = type(arg_val)
                soap_type = PYTHON_TO_SOAP_TYPE_MAP[py_type]

                if soap_type == 'xsd:string':
                    arg_val = bytes_cast(arg_val)
                elif soap_type == 'xsd:int' or soap_type == 'xsd:float':
                    arg_val = str(argval)
                elif soap_type == 'xsd:boolean':
                    arg_val = "1" if arg_val else "0"

                argElement = SubElement(methElement, arg_name)
                if typed and arg_type:
                    if not isinstance(type, QName):
                        arg_type = QName(NS_XSD, arg_type)
                    argElement.set(NS_XSI + "type", arg_type)

                argElement.text = arg_val
        else:
            methElement.text = ""

        envelope_content = xml_tostring(envelope, short_empty_elements=False)
        content = XML_DOCUMENT_DECLARATION + str_cast(envelope_content)

        return content

    def create_response(self, action_name: str, arguments: dict, encoding=None, envelope_attrib=None, typed=None):

        register_namespace('', None)

        if encoding is None:
            encoding = self._encoding
        if envelope_attrib is None:
            envelope_attrib = self._envelope_attrib
        if typed is None:
            typed = self._typed

        envelope = Element("s:Envelope")
        if envelope_attrib:
            for eakey, eaval in envelope_attrib:
                envelope.attrib.update({eakey: eaval})
        else:
            envelope.attrib.update({'xmlns:s': NS_SOAP_ENV})
            envelope.attrib.update({'s:encodingStyle': encoding})

        body = SubElement(envelope, "s:Body")

        action_name_tag_name = action_name + "Response"
        methElement = SubElement(body, action_name_tag_name)
        if encoding:
            methElement.set(NS_SOAP_ENV + "encodingStyle", encoding)

        if arguments:
            for arg_name, arg_val in arguments.items():
                py_type = type(arg_val)
                soap_type = PYTHON_TO_SOAP_TYPE_MAP[py_type]

                if soap_type == 'xsd:string':
                    arg_val = bytes_cast(arg_val)
                elif soap_type == 'xsd:int' or soap_type == 'xsd:float':
                    arg_val = str(argval)
                elif soap_type == 'xsd:boolean':
                    arg_val = "1" if arg_val else "0"

                argElement = SubElement(methElement, arg_name)
                if typed and arg_type:
                    if not isinstance(type, QName):
                        arg_type = QName(NS_XSD, arg_type)
                    argElement.set(NS_XSI + "type", arg_type)

                argElement.text = arg_val
        else:
            methElement.text = ""

        envelope_content = xml_tostring(envelope, short_empty_elements=False)
        content = XML_DOCUMENT_DECLARATION + "\n" + str_cast(envelope_content)

        return content

    def parse_response(self, action_name, content, encoding=None, envelope_attrib=None, typed=None):

        register_namespace('', None)

        if encoding is None:
            encoding = self._encoding
        if envelope_attrib is None:
            envelope_attrib = self._envelope_attrib
        if typed is None:
            typed = self._typed

        try:
            docNode = xml_fromstring(content)
        except ParseError as perr:
            # Try removing any extra XML declarations in case there are more than one.
            # This sometimes happens when a device sends its own XML config files.
            docNode = xml_fromstring(self._remove_extraneous_xml_declarations(content))
        except ValueError as verr:
            # This can occur when requests returns a `str` (unicode) but there's also an XML
            # declaration, which lxml doesn't like.
            docNode = xml_fromstring(content.encode('utf8'))

        if typed:
            resp_body = docNode.find(".//{%s}%sResponse" % (typed, action_name))
        else:
            resp_body = docNode.find(".//%sResponse" % action_name)

        if resp_body is None:
            msg = ('Returned XML did not include an element which matches namespace %r and tag name'
                   ' \'%sResponse\'.' % (typed, action_name))
            print(msg + '\n' + xml_tostring(xml, short_empty_elements=False).decode('utf8'))
            raise SOAPProtocolError(msg)

        # Sometimes devices return XML strings as their argument values without escaping them with
        # CDATA. This checks to see if the argument has been parsed as XML and un-parses it if so.
        resp_dict = {}
        for arg in resp_body.getchildren():
            children = arg.getchildren()
            if children:
                resp_dict[arg.tag] = b"\n".join(xml_tostring(x) for x in children)
            else:
                resp_dict[arg.tag] = arg.text

        return resp_dict

