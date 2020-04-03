

from xml.etree.ElementTree import Element, SubElement, QName
from xml.etree.ElementTree import tostring as xml_tostring

from akit.compat import bytes_cast, str_cast

NS_SOAP_ENV = "http://schemas.xmlsoap.org/soap/envelope/"
NS_SOAP_ENC = "http://schemas.xmlsoap.org/soap/encoding/"
NS_XSI = "http://www.w3.org/1999/XMLSchema-instance"
NS_XSD = "http://www.w3.org/1999/XMLSchema"

URI_SOAP_ENCODING = "http://schemas.xmlsoap.org/soap/encoding/"

XML_DOCUMENT_DECLARATION = """<?xml version="1.0" encoding="utf-8"?>"""

PYTHON_TO_SOAP_TYPE_MAP = {
    bytes: 'xsd:string',
    str: 'xsd:string',
    int: 'xsd:int',
    float: 'xsd:float',
    bool: 'xsd:boolean'
}

class SoapRequestBuilder:

    def __init__(self, encoding=SOAP_ENCODING, envelope_attrib=None, typed=None):
        self._encoding = encoding
        self._envelope_attrib = envelope_attrib
        self._typed = typed
        return

    def create_request(self, method: str, arguments: dict, encoding=None, envelope_attrib=None, typed=None):

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

        methElement = SubElement(body, method)
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
            methElement.append({})

        content = XML_DOCUMENT_DECLARATION + "\n" + xml_tostring(envelope, 'utf-8')

        return content


class SoapResponseBuilder:

    def __init__(self, encoding=SOAP_ENCODING, envelope_attrib=None, typed=None):
        self._encoding = encoding
        self._envelope_attrib = envelope_attrib
        self._typed = typed
        return

    def create_response(self, method: str, arguments: dict, encoding=None, envelope_attrib=None, typed=None):

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

        method_tag_name = method + "Response"
        methElement = SubElement(body, method_tag_name)
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
            methElement.append({})

        content = XML_DOCUMENT_DECLARATION + "\n" + xml_tostring(envelope, 'utf-8')

        return content
