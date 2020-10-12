
from akit.environment.console import showlog
from akit.integration.landscaping import Landscape

showlog()

print("Preparing Landscape...")

lscape = Landscape()
lscape.first_contact()

print("Landscape Initialized...")
print("")
print("Use 'lscape' variable to access the global Landscape instance")
