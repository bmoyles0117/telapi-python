from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class MMSMessage(InstanceResource):
    pass
    
class MMSMessages(ListResource):
    instance_resource = MMSMessage