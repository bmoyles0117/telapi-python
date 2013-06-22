from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Usage(InstanceResource):
    pass
    
class Usages(ListResource):
    instance_resource = Usage