#!/usr/bin/python

import  socket,time
import thread
#import the required module for text
#to speech conversion

from gtts import gTTS

#this module is imported so that we can play converted audio
import os

import pyttsx
engine = pyttsx.init()
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)





while 4>2:
	msg=raw_input("enter a message to send : ")
		
	q=s.sendto(msg,("192.168.43.102",9999))
	data=s.recvfrom(1000)
	engine.say(data[0])
	engine.say("   ")
	engine.runAndWait()	


