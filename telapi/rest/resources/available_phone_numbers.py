from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class AvailablePhoneNumber(InstanceResource):
    def purchase(self):
        return self.ancestor_resource.incoming_phone_numbers.create(phone_number=self.phone_number)
    
class AvailablePhoneNumbers(ListResource):
    instance_resource = AvailablePhoneNumber
    
    def get_resource_path(self):
        return 'AvailablePhoneNumbers/US/Local'