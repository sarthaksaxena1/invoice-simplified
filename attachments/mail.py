import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import sys 
import os
name = sys.argv[1]
partcipantEmail=sys.argv[2]
newFileNames=['final.zip']
fromaddr = sys.argv[3]
finalmsglist=[]
password=sys.argv[4]


def Create_Email_Body(newFileNames,participantEmail,name,password):
	# fromaddr = "itclpu@vanshdevgan.co"
	fromaddr = sys.argv[3]
	toaddr = partcipantEmail

        # instance of MIMEMultipart
	msg = MIMEMultipart()

        # storing the senders email address
	msg['From'] = fromaddr

        # storing the receivers email address
	msg['To'] = toaddr

        # storing the subject
	msg['Subject'] = "INVOICE MADE SIMPLE -"

        # string to store the body of the mail
	body = "Dear " + name + " , Find Your Files Attached In Zip File Below "
        # attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))
        # open the file to be sent
	print("Preparing Files ....")
	filename = "final.zip"
	attachment = open(filename, "rb")

        # instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
	p.set_payload((attachment).read())

        # encode into base64
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # attach the instance 'p' to instance 'msg'
	msg.attach(p)
        # Converts the Multipart msg into a string
	finalmsgtext = msg.as_string()
	finalmsglist.append(finalmsgtext)
def SendEmailToALL(partcipantEmail,password):
	s = smtplib.SMTP('mail.vanshdevgan.co',26)
	s.starttls()
	s.login(fromaddr, password)
	message = finalmsglist[0]
	print("Sending Email To : ", partcipantEmail)
	s.sendmail(fromaddr,partcipantEmail,message)
	print(" Email Sent To : ", partcipantEmail)
	s.quit()



print("Check Your Details Below : \n")
print("\n RECEIVER NAME : ",name)
print("\n RECEIVER EMAIL : ",partcipantEmail)
print("\n SENDER EMAIL : ",fromaddr,)
print("\n Password You Enter : ",password)
print("\n \n [1] Confirm Details")
print("\n \n [2] Exit & Restart")
opt=int(input("Choose Option Given Below"))
if(opt==1):
	Create_Email_Body(newFileNames,partcipantEmail,name,password)
	SendEmailToALL(partcipantEmail,password)
elif(opt==2):
	exit(1)
