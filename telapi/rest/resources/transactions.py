from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Transaction(InstanceResource):
    pass
    
class Transactions(ListResource):
    instance_resource = Transaction