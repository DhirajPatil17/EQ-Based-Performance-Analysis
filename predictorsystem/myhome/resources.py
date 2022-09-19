from import_export import resources
from .models import Fyit, Syit, visualize

class visualizeResources(resources.ModelResource):
    class meta:
        model=visualize
class FyitResources(resources.ModelResource):
    class meta:
        model=Fyit
class SyitResources(resources.ModelResource):
    class meta:
        model=Syit