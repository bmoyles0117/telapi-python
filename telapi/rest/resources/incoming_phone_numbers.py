from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class IncomingPhoneNumber(InstanceResource):
    pass
    
class IncomingPhoneNumbers(ListResource):
    instance_resource = IncomingPhoneNumber
    
    def get_resource_path(self):
        return self.__class__.__name__