from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Fax(InstanceResource):
    pass
    
class Faxes(ListResource):
    instance_resource = Fax