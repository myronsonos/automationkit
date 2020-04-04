"""
.. module:: akit.integration.upnp.extensions.services.standard.contentdirectory
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing :class:`ContentDirectoryService` which implements
    the standard UPNP ContentDirectory service.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = ""

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class BrowseFlags:
    BrowseDirectChildren = "BrowseDirectChildren"
    BrowseMetadata = "BrowseMetadata"

class ContentDirectoryService(UpnpServiceProxy, LoadableExtension):
    """
    """

    SERVICE_ID = "urn:schemas-upnp-org:serviceId:ContentDirectory"
    SERVICE_TYPE = "urn:schemas-upnp-org:service:ContentDirectory:1"

    def Browse(self, ObjectID: str = "0", BrowseFlag: str = "BrowseDirectChildren", Filter: str = "*", StartingIndex: int = 0, RequestedCount: int = 10, SortCriteria: str = None):
        """

        Returns:
            { 'Result': ?, 'NumberReturned': ?, 'TotalMatches': ?, 'UpdateID': ? }
        """
        args = { "ObjectID": ObjectID, "BrowseFlag": BrowseFlag, "Filter": Filter, "StartingIndex": StartingIndex, "RequestedCount": RequestedCount, "SortCriteria": SortCriteria }
        rtnobj = self.call_action("FindPrefix", args)
        return rtnobj

    def FindPrefix(self, ObjectID: str, Prefix: str = None):
        """
        Returns:
            { 'StartingIndex': ?, 'UpdateID': ? }
        """
        args = { "ObjectID": ObjectID, "Prefix": Prefix }
        rtnobj = self.call_action("FindPrefix", args)
        return rtnobj

    def GetSearchCapabilities(self):
        """
        Returns:
            { 'SearchCaps': ? }
        """
        rtnobj = self.call_action("GetSearchCapabilities")
        return rtnobj

    def GetSortCapabilities(self):
        """
        Returns:
            { 'SortCapabilities': ? }
        """
        rtnobj = self.call_action("GetSortCapabilities")
        return rtnobj

    def GetSystemUpdateID(self):
        """
        Returns:
            { 'Id': ? }
        """
        rtnobj = self.call_action("GetSystemUpdateID")
        return rtnobj

    def GetAlbumArtistDisplayOption(self):
        """
        Returns:
            { 'AlbumArtistDisplayOption': ? }
        """
        rtnobj = self.call_action("GetAlbumArtistDisplayOption")
        return rtnobj

    def GetLastIndexChange(self):
        """
        Returns:
            { 'LastIndexChange': ? }
        """
        rtnobj = self.call_action("GetLastIndexChange")
        return rtnobj

    def GetAllPrefixLocations(self, ObjectID: str):
        """
        Returns:
            { 'TotalPrefixes': ?, 'PrefixAndIndexCSV': ?, 'UpdateID': ? }
        """
        args = { "ObjectID": ObjectID }
        rtnobj = self.call_action("GetAllPrefixLocations", args)
        return rtnobj

 
    def CreateObject(self, ContainerID: str, Elements: str):
        """
        Returns:
            { 'ObjectID': ?, 'Result': ? }
        """
        args = { "ContainerID": ContainerID, "Elements": Elements }
        rtnobj = self.call_action("CreateObject", args)
        return rtnobj

    def UpdateObject(self, ObjectID: str, CurrentTagValue: str, NewTagValue: str):
        """
        Returns:
            { 'ObjectID': ?, 'Result': ? }
        """
        args = { "ObjectID": ObjectID, "CurrentTagValue": CurrentTagValue, "NewTagValue": NewTagValue }
        rtnobj = self.call_action("UpdateObject", args)
        return rtnobj

    def DestroyObject(self, ObjectID: str):
        """
        """
        args = { "ObjectID": ObjectID }
        rtnobj = self.call_action("DestroyObject", args)
        return rtnobj

    def RefreshShareIndex(self, AlbumArtistDisplayOption: str):
        """
        """
        args = { "AlbumArtistDisplayOption": AlbumArtistDisplayOption }
        rtnobj = self.call_action("RefreshShareIndex", args)
        return rtnobj

    def RequestResort(self, SortOrder: str):
        """
        """
        args = { "SortOrder": SortOrder }
        rtnobj = self.call_action("RequestResort", args)
        return rtnobj

    def GetShareIndexInProgress(self):
        """
        Returns:
            { 'IsIndexing': ? }
        """
        rtnobj = self.call_action("GetShareIndexInProgress")
        return rtnobj

    def GetBrowseable(self):
        """
        Returns:
            { 'IsBrowseable': ? }
        """
        rtnobj = self.call_action("GetBrowseable")
        return rtnobj

    def SetBrowseable(self, Browseable: bool):
        """
        Returns:
            { 'IsBrowseable': ? }
        """
        args = { "Browseable": Browseable }
        rtnobj = self.call_action("SetBrowseable", args)
        return rtnobj

if __name__ == "__main__":
    host = "192.168.1.42:1400"
    baseURL = "http://192.168.1.42:1400"
    controlURL = "/MediaServer/ContentDirectory/Control"
    eventSubURL  = "/MediaServer/ContentDirectory/Event"
    cdsvc = ContentDirectoryService()
    cdsvc.set_call_parameters(host, baseURL, controlURL, eventSubURL)

    browseable = cdsvc.GetBrowseable()

    print(browseable)

    print("")