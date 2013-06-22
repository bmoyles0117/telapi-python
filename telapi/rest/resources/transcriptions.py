from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource

class Transcription(InstanceResource):
    pass
    
class Transcriptions(ListResource):
    instance_resource = Transcription