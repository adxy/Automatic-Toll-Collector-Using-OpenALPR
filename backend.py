import os
import httplib2
from flask import Flask
from flask import render_template, request, redirect
from detection import getLP
#from send_email_main import send_email_from_backend_with_attachment
from send_sms import sendSMS

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

imageSavePath = APP_ROOT + "/static/"

#Set True to send and False to Not Send
sms = True
email = False

#Index Page
@app.route('/')
def index():
    return render_template('index.html')

#When user clicks on upload button this activates
@app.route("/upload-image", methods=["GET","POST"])
def upload_image():

	
	if request.method == "POST":

		if request.files:

			image = request.files["image"]

			image.save(os.path.join(imageSavePath, image.filename))

			print("Image saved")

			imageLocation= "static/" + image.filename 

			# GET LP NUMBER AND STORE IN INFO

			info = getLP(imageLocation)

			#EMAIL BODY CONTENT
			email_content = f"Welcome to New Delhi! Your Vehicle with License Plate Number {info} just enterd Delhi from our Toll. We have deducted Rs.80 from your account."

			# EMAIL ATTACHMENT DIRECTORY

			cwd = os.getcwd()

			image_dir = cwd +"/"+ imageLocation

			#Setting status as "Not sent" for default

			errorMessage = "Failed! Maybe try a clearer image!"

			if info == errorMessage:

				sms_status = "Not Sent"
				email_status = "Not Sent"

					
			else:

				#SEND EMAIL IF TRUE

				if email:
					email_status = "Sent Successfully!"

					send_email_from_backend_with_attachment(email_content, image_dir)

				else:
					email_status = "Turned off by user Manually!"

				#SEND SMS IF TRUE

				if sms:
					sms_status = "Sent Successfully!"

					sendSMS(info)		
				else:

					sms_status = "Turned off by user Manually!"

			#return redirect(request.url)


	#OPENS RESULTS PAGE
	return render_template("results.html", info= info,imageLocation= imageLocation, sms_status = sms_status, email_status=email_status)
