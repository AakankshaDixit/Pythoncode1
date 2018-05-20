#!/usr/bin/python

import  socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

t=time.time()+10
while time.time()<t:
	msg=raw_input("enter a message to send : ")
	q=s.sendto(msg,("192.168.43.102",9999))
	#print s.recvfrom(1000)
