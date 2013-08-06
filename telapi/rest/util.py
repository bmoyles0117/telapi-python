OUTBOUND_PARAMETER_MAP = {
    'attachment'                : 'Attachment',
    'audio_direction'           : 'AudioDirection',
    'audio_url'                 : 'AudioUrl',
    'body'                      : 'Body',
    'callback_url'              : 'CallbackUrl',
    'date_created'              : 'DateCreated',
    'date_updated'              : 'DateUpdated',
    'direction'                 : 'Direction',
    'fallback_method'           : 'FallbackMethod',
    'fallback_url'              : 'FallbackUrl',
    'file_format'               : 'FileFormat',
    'forwarded_from'            : 'ForwardedFrom',
    'friendly_name'             : 'FriendlyName',
    'from_'                     : 'From',
    'heartbeat_method'          : 'HeartbeatMethod',
    'heartbeat_url'             : 'HeartbeatUrl',
    'hide_caller_id'            : 'HideCallerId',
    'if_machine'                : 'IfMachine',
    'if_machine_method'         : 'IfMachineMethod',
    'if_machine_url'            : 'IfMachineUrl',
    'length'                    : 'Length',
    'loop'                      : 'Loop',
    'method'                    : 'Method',
    'mix'                       : 'Mix',
    'page'                      : 'Page',
    'page_size'                 : 'PageSize',
    'phone_number'              : 'PhoneNumber',
    'pitch'                     : 'Pitch',
    'pitch_octaves'             : 'PitchOctaves',
    'pitch_semi_tones'          : 'PitchSemiTones',
    'play_dtmf'                 : 'PlayDtmf',
    'play_dtmf_direction'       : 'PlayDtmfDirection',
    'rate'                      : 'Rate',
    'record'                    : 'Record',
    'record_callback'           : 'RecordCallback',
    'send_digits'               : 'SendDigits',
    'status'                    : 'Status',
    'status_callback'           : 'StatusCallback',
    'status_callback_method'    : 'StatusCallbackMethod',
    'straight_to_voicemail'     : 'StraightToVoicemail',
    'tempo'                     : 'Tempo',
    'time_limit'                : 'TimeLimit',
    'timeout'                   : 'Timeout',
    'transcribe'                : 'Transcribe',
    'transcribe_callback'       : 'TranscribeCallback',
    'to'                        : 'To',
    'url'                       : 'Url'
}

def transform_camels(value, transform_callback):
    return ''.join([transform_callback(x) if x.isupper() and not value[min(i + 1, len(value))].istitle() else x for i, x in enumerate(value)])

def transform_params(params):
    return dict((OUTBOUND_PARAMETER_MAP.get(k, k), v, ) for k, v in params.items())

def camel_to_underscore(value):
    return (value[0] + transform_camels(value[1:], lambda x: '_' + x)).lower()

def camel_to_slashes(value):
    return value[0] + transform_camels(value[1:], lambda x: '/' + x)

# Reverse the outbound parameter map to create an inbound map
INBOUND_PARAMETER_MAP = dict((y, x, ) for (x, y, ) in OUTBOUND_PARAMETER_MAP.items())