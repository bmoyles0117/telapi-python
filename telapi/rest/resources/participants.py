from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Participant(InstanceResource):
    pass
    
class Participants(ListResource):
    instance_resource = Participant