from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(

    #Replace this sample phone number with your actual phone number you used when you created Twilio account
    to="+10123456789",
    
    #Replace this sample phone number with the one that Twilio gave you which can be found on your Twilio account
    from_="+19999999999",
    body="Wow! It works! loving it :)")

print(message.sid)
