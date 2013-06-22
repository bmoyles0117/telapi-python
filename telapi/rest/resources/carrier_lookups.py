from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class CarrierLookup(InstanceResource):
    pass
    
class CarrierLookups(ListResource):
    instance_resource = CarrierLookup
    
    def search(self, phone_number):
        return self.filter(phone_number=phone_number)[0]
    
    def get_resource_path(self):
        return 'Carrier'