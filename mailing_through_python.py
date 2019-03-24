import smtplib
import os
import imghdr #to determine the extension of the image
from email.message import EmailMessage 

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS') #gets the email address that was set in the environmental variable
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD') #gets the password of the email

RECEIVER = 'hamzza151817@gmail.com'
SENDER = EMAIL_ADDRESS #since i'll be the one sending emails to others

contacts = ['hamzza151817@gmail.com', 'testuser@gmail.com']

message = EmailMessage()

message['Subject'] = 'Subject of an email'
message['From'] = SENDER
#For multiple receivers
message['To'] = ', '.join(contacts) #according to the documentation
message.set_content = 'Message of an email'


#Secure Shell method for sending the emails
def smtp_ssl(message, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD):
	'''Using SMTP_SSL method for sending mails conveniently'''

	#Using context manager for efficiently closing off our connection
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #For plain smtp the port is 587
		smtp.login(email_address, email_password)

		smtp.send_message(message)

# smtp_ssl(message, SENDER, EMAIL_PASSWORD)


picture_files = ['image_1.jpeg', 'image_2.jpeg']

def attachingPictures(message, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD):
	for file in picture_files:
		with open(file, 'rb') as f:
			file_data = f.read()
			file_name = f.name
			file_type = imghdr.what(file_name) #returns the extension of the image

		message.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(email_address, email_password)	
		smtp.send_message(message)


def html_based_mails(message, email_address, email_password):
	message.add_alternative(
		'''\
		<!DOCTYPE html>
		<html>
			<body>
					<h1 style='color:SlateGray;'>
						This is an Html Email.
					</h1>
			</body>
		</html>
		''', subtype='html')

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(email_address, email_password)
		smtp.send_message(message)




pdf_files = []

def sendingPDF(message, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD):
	for file in pdf_files:
		with open(file, 'rb') as f:
			file_data = f.read()
			file_name = f.name

		message.add_attachment(file_data, maintype='application', subtype='octect-stream', filename=file_name)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(email_address, email_password)

		smtp.send_message(message)


#A simple plain method of smtp to send the emails
def simple_smtp():
	'''A simple smtp method to send the email'''

	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo() #Identifies the mail server 
		smtp.starttls() #For encryption
		smtp.ehlo()

		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

		subject = "Subject for the mail"
		body = "The body of the rest of the mail"

		message = f'Subject: {subject}\n\n{body}'

		smtp.sendmail(SENDER, RECEIVER, message)


#For converting our shell into a server that will listen to our mails
'''python3 -m smtpd -c DebuggingServer -n localhost:9675''' 
#For linux and mac

#A method for debugging the smtp and the emails to be sent
def debugging_smtp_mails():
	#Debugging our emails
	with smtplib.SMTP('localhost', 9675) as smtp:

		subject = "Subject for the mail"
		body = "The body of the rest of the mail"

		message = f'Subject: {subject}\n\n Body:{body}'

		smtp.sendmail(SENDER, RECEIVER, message)
