# Licensed under the MIT license
# http://opensource.org/licenses/mit-license.php

# Copyright 2007 - Frank Scholz <coherence@beebits.net>

from twisted.python import failure

from coherence import log
from coherence.compat import bytes_cast, bytes_convert, str_cast
from coherence.extern.et import ET, namespace_map_update

from coherence.upnp.core.utils import getPage, parse_xml

from coherence.upnp.core import soap_lite


class SOAPProxy(log.Loggable):
    """ A Proxy for making remote SOAP calls.

        Based upon twisted.web.soap.Proxy and
        extracted to remove the SOAPpy dependency

        Pass the URL of the remote SOAP server to the constructor.

        Use proxy.callRemote('foobar', 1, 2) to call remote method
        'foobar' with args 1 and 2, proxy.callRemote('foobar', x=1)
        will call foobar with named argument 'x'.
    """

    logCategory = 'soap'

    def __init__(self, url, namespace=None, envelope_attrib=None, header=None, soapaction=None):
        log.Loggable.__init__(self)
        self.url = bytes_cast(url)
        self.namespace = bytes_cast(namespace)
        self.header = bytes_cast(header)
        self.action = None
        self.soapaction = bytes_cast(soapaction)
        self.envelope_attrib = bytes_cast(envelope_attrib)

    def callRemote(self, soapmethod, arguments):

        bytes_arguements = bytes_convert(arguments)
        soapaction = bytes_cast(soapmethod or self.soapaction)
        if b'#' not in soapaction:
            soapaction = b'#'.join((self.namespace[1], soapaction))

        self.action = soapaction.split(b'#')[1]

        self.info("callRemote ns=%r sact=%r smeth=%r act=%r", self.namespace, self.soapaction, soapmethod, self.action)

        # Prep the call, convert all the strings to bytes

        headers = {
            b'content-type': b'text/xml ;charset="utf-8"',
            b'SOAPACTION': b'"%s"' % soapaction, }
        if 'headers' in bytes_arguements:
            headers.update(bytes_arguements[b'headers'])
            del bytes_arguements[b'headers']

        payload = soap_lite.build_soap_call("{%s}%s" % (self.namespace[1], self.action), bytes_arguements,
                                            encoding=None)

        self.info("callRemote soapaction:  %s %s", self.action, self.url)
        self.debug("callRemote payload:  %s", payload)

        def gotError(error, url):
            self.warning("error requesting url %r", url)
            self.debug(error)
            try:
                tree = parse_xml(error.value.response)
                body = tree.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')
                return failure.Failure(Exception("%s - %s" % (body.find('.//{urn:schemas-upnp-org:control-1-0}errorCode').text,
                                                    body.find('.//{urn:schemas-upnp-org:control-1-0}errorDescription').text)))
            except:
                import traceback
                self.debug(traceback.format_exc())
            return error

        page_result = getPage(self.url, postdata=payload, method="POST", headers=headers).addCallbacks(
            self._cbGotResult, gotError, None, None, [self.url], None)

        return page_result

    def _cbGotResult(self, result):
        #print(("_cbGotResult 1", result))
        page, headers = result
        #result = SOAPpy.parseSOAPRPC(page)
        #print(("_cbGotResult 2", result))

        def print_c(e):
            for c in e.getchildren():
                print((c, c.tag))
                print_c(c)

        self.debug("result: %r", page)

        tree = parse_xml(page)
        #print((tree, "find %s" % self.action))

        #root = tree.getroot()
        #print_c(root)

        body = tree.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')
        #print(("body", body))
        response = body.find('{%s}%sResponse' % (self.namespace[1], self.action))
        if response == None:
            """ fallback for improper SOAP action responses """
            response = body.find('%sResponse' % self.action)
        self.debug("callRemote response  %s", response)
        result = {}
        if response != None:
            for elem in response:
                result[elem.tag] = soap_lite.decode_result(elem)
        #print(("_cbGotResult 3", result))

        return result
