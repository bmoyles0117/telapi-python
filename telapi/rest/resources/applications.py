from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Application(InstanceResource):
    pass
    
class Applications(ListResource):
    instance_resource = Application