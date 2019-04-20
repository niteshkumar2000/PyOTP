from twilio.rest import Client
account_sid = 'ACe2c5ecf2d590efd7f3afdceeb68b73d6' # Found on Twilio Console Dashboard
auth_token = '9733089d5e44e4eed34c944a7a79e153' # Found on Twilio Console Dashboard

myPhone = '+918825812533' # Phone number you used to verify your Twilio account
TwilioNumber = '+19282715475' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)

call = client.calls.create(
		  to=myPhone,
		  from_=TwilioNumber,
			url = "http://demo.twilio.com/docs/voice/xml"
	)

print(call.sid)
 