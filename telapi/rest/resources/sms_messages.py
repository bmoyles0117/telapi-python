from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class SMSMessage(InstanceResource):
    pass
    
class SMSMessages(ListResource):
    instance_resource = SMSMessage