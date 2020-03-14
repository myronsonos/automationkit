
from akit.integration.landscaping import Landscape, LandscapeDescription
from akit.xlogging import getAutomatonKitLogger

from somens.integration.clients.linuxclient import LinuxClientMixIn
from somens.integration.clients.linuxclient import WindowsClientMixIn
from somens.integration.cluster.clustermixin import ClusterMixIn
from somens.integration.playback.playbackdevicemixin import PlaybackDeviceMixIn

logger = getAutomatonKitLogger()

class SomeLandscapeDescription(LandscapeDescription):

    @classmethod
    def register_integration_points(cls, landscape):
        landscape.register_integration_point("primary-linux", LinuxClientMixIn)
        landscape.register_integration_point("secondary-linux", LinuxClientMixIn)

        landscape.register_integration_point("primary-windows", WindowsClientMixIn)
        landscape.register_integration_point("secondary-windows", WindowsClientMixIn)

        landscape.register_integration_point("primary-cluster", ClusterMixIn)
        landscape.register_integration_point("secondary-cluster", ClusterMixIn)

        landscape.register_integration_point("primary-playback", PlaybackDeviceMixIn)
        landscape.register_integration_point("secondary-playback", PlaybackDeviceMixIn)
        return


class SomeLandscape(Landscape):
    """
        This is a mock test landscape integration derivative component.
    """
    landscape_description = SomeLandscapeDescription

    def initialize(self):
        super(SomeLandscape, self).initialize()
        return

    def diagnostic(self, diaglabel, diags):
        """
            Can be called in order to perform a diagnostic capture across the test landscape.
        """
        diagmsg = "Diagnostics were run label=%s\n" % diaglabel

        for dkey, dval in diags.items():
            diagmsg += "    %s: %s\n" % (dkey, dval)

        logger.info(diagmsg)
        return
    
    def first_contact(self):
        """
            This method should be called as early as possible in order to ensure the entities in the
            automation landscape exist and the authentication credentials provided for these entities are
            valid and usable to interact with these entities.

            :returns list: list of failing entities
        """
        return


