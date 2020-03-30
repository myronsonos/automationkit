
from coherence.upnp.core.utils import getPage
from coherence.backend import BackendItem, BackendStore

from coherence.extern.simple_plugin import Plugin

from coherence import log


class SonosDevice(log.Loggable):
    logCategory = 'sonos_household'

    implements = ['MediaRenderer']

    def __init__(self, id, obj, parent, mimetype, urlbase, UPnPClass, store=None, update=False, proxy=False):
        return

class SonosHousehold(log.Loggable, Plugin):
    """
        This plugin registeres our sonos household with Coherence.
    """
    logCategory = 'sonos_household'

    implements = ['MediaServer']

    def __init__(self, server, **kwargs):
        return