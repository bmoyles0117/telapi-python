from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource
from telapi.rest.resources.participants import Participants

class Conference(InstanceResource):
    subresources = [Participants]
    
class Conferences(ListResource):
    instance_resource = Conference