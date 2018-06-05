#!/usr/bin/python

import  socket,time
import thread
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



def sender():

	while True:
		msg=raw_input("enter a message to send : ")
		
		q=s.sendto(msg,("192.168.10.164",9999))
		print s.recvfrom(1000)
		

thread.start_new_thread(sender,())

while True:
	pass
