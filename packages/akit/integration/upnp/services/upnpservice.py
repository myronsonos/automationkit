

class UpnpService:
    """
    """

    SERVICE_ID = None
    SERVICE_TYPE = None

    def __init__(self):
        self._destription = None
        return

    def update_description(self, destription):
        self._destription = destription
        return