from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Recording(InstanceResource):
    pass
    
class Recordings(ListResource):
    instance_resource = Recording