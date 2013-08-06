from telapi.rest.resources.applications import Applications
from telapi.rest.resources.base import InstanceResource
from telapi.rest.resources.base import ListResource
from telapi.rest.resources.available_phone_numbers import AvailablePhoneNumbers
from telapi.rest.resources.bna_lookups import BNALookups
from telapi.rest.resources.calls import Calls
from telapi.rest.resources.carrier_lookups import CarrierLookups
from telapi.rest.resources.cnam_lookups import CNAMLookups
from telapi.rest.resources.conferences import Conferences
from telapi.rest.resources.faxes import Faxes
from telapi.rest.resources.incoming_phone_numbers import IncomingPhoneNumbers
from telapi.rest.resources.mms_messages import MMSMessages
from telapi.rest.resources.notifications import Notifications
from telapi.rest.resources.recordings import Recordings
from telapi.rest.resources.sms_messages import SMSMessages
from telapi.rest.resources.transactions import Transactions
from telapi.rest.resources.transcriptions import Transcriptions
from telapi.rest.resources.usages import Usages

class Account(InstanceResource):
    subresources = [
        Applications, AvailablePhoneNumbers, BNALookups, Calls, CarrierLookups, 
        CNAMLookups, Conferences, Faxes, IncomingPhoneNumbers, MMSMessages, Notifications,
        Recordings, SMSMessages, Transactions, Transcriptions, Usages
    ]

class Accounts(ListResource):
    instance_resource = Account