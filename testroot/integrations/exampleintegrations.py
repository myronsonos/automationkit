
from akit.mixins.integration import IntegrationMixIn

class ExampleIntegrationMixIn(IntegrationMixIn):
    
    @classmethod
    def attach_to_environment(cls):
        
        return

    @classmethod
    def collect_resources(cls):
        
        return

    @classmethod
    def diagnostic(cls, diag_level, diag_folder):
        
        return

    @classmethod
    def establish_connectivity(cls):
        
        return
