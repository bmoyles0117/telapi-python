# TelAPI Python

### Create an Account object
Account objects will be used to perform all actions available for your TelAPI account. Authenticating is easy, and you may then use the account object anywhere else in your code.

```python
import telapi.rest

try:
    account = telapi.rest.authenticate('ACCOUNT_SID', 'AUTH_TOKEN')
    
    # ... code examples from below, here

except telapi.rest.AuthenticationError, e:
    print "Failed to authenticate: %s" % (e, )
```

### Create a Call
```python
try:
    call = account.calls.create(from_='+15555555555', to="+15558884341", url="http://...")

    print "Successful Call: %s" % (call.sid, )
except telapi.rest.RestError, e:
    print "Error creating a call: %s" % (e, )
```

### Send an SMS Message
```python
try:
    sms_message = account.sms_messages.create(
        from_='+15555555555', to="+15558884341", body="Hello world"
    )
    
    print "Successful SMS Message: %s" % (sms_message.sid, )
except telapi.rest.RestError, e:
    print "Error creating an sms message: %s" % (e, )
```

### Carrier Lookups
```python
try:
    carrier_lookup = account.carrier_lookups.search('+15558884341')

    print "Successful Lookup: %s" % (carrier_lookup.sid, )
except telapi.rest.RestError, e:
    print "Carrier lookup failed: %s" % (e, )
```
