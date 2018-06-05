#!/usr/bin/python3

import smtplib
import config

#sender_mail=input("enter the sender mail")
#sender_passwd=input("enter the password")

#receiver_mail=input("enter the receiver mail")
#...function for sending the mail
def send_mail(subject,msg):
	try:
		server=smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(config.sender_email,config.sender_passwd)
		message = 'Subject:{}  {}'.format(subject,msg)
		server.sendmail(config.sender_email,config.receiver_email,message)
		server.quit()
		print("Success : Email sent !")
	except:
		print("Email failed to send !")

subject = "testing"
msg = "hello there,who's you?"

send_mail(subject,msg) 

