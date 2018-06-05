#!/usr/bin/python

import  socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

t=0
while t<10:
	msg=raw_input("enter a message to send : ")
	q=s.sendto(msg,("192.168.10.62",9999))
	#print s.recvfrom(1000)
	t=t+1

	

