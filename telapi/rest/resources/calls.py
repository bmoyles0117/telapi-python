from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource
from telapi.rest.resources.recordings import Recordings

class Call(InstanceResource):
    BUSY        = "busy"
    CANCELED    = "canceled"
    COMPLETED   = "completed"
    FAILED      = "failed"
    IN_PROGRESS = "in-progress"
    NO_ANSWER   = "no-answer"
    QUEUED      = "queued"
    RINGING     = "ringing"
    
    subresources = [Recordings]
    
    def hangup(self):
        return self.update(status=Call.COMPLETED)
    
    def send_digits(self, dtmf, direction = 'in'):
        return self.update(play_dtmf=dtmf, play_dtmf_direction=direction)
    
class Calls(ListResource):
    instance_resource = Call