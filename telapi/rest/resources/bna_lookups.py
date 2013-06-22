from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class BNALookup(InstanceResource):
    pass
    
class BNALookups(ListResource):
    instance_resource = BNALookup
    
    def get_resource_path(self):
        return 'BNA'