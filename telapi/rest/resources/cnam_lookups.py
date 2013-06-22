from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class CNAMLookup(InstanceResource):
    pass
    
class CNAMLookups(ListResource):
    instance_resource = CNAMLookup
    
    def get_resource_key(self):
        return 'cnam_dips'
    
    def get_resource_path(self):
        return 'CNAM'