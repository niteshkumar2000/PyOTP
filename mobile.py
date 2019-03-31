from textmagic.rest import TextmagicRestClient
  
username = "pycoders2432"
token = "pyotp2432"
client = TextmagicRestClient(username, token)
  
message = client.messages.create(phones="8825812533", text="Hello TextMagic")