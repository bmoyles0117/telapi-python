from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Notification(InstanceResource):
    pass
    
class Notifications(ListResource):
    instance_resource = Notification