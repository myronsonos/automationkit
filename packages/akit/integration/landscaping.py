"""
.. module:: akit.integration.landscape
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`TestLandscape` class and associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

class LandscapeDescription:
    """
    """

    def load(self, landscapefile):
        return
    

class Landscape:
    """
    """

    def diagnostic(self, diaglabel, diags):
        """
            Can be called in order to perform a diagnostic capture across the test landscape.
        """
        return
    
    def first_contact(self):
        """
            This method should be called as early as possible in order to ensure the entities in the
            automation landscape exist and the authentication credentials provided for these entities are
            valid and usable to interact with these entities.

            :returns list: list of failing entities
        """
        return
