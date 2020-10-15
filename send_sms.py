from twilio.rest import Client


def sendSMS(plate):

	account_sid = 'your twilio sid id here'
	auth_token = 'your twilio authentication token here'
	client = Client(account_sid, auth_token)

	message = client.messages.create(
	         body=f"Welcome to Delhi! Your Vehcile with LP Number {plate} just crossed the New Delhi toll, amount of Rs. 80 has been deducted from your account.",
	         from_='+18564816686',
	         to='+919821922838'
	     )

	print(f"this is message sid {message.sid}")
