#!/usr/bin/python

import  socket,time 
import thread
rec_ip="192.168.10.164"
myport=9999
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 
t=time.time()+10
def recv():
	while True:

		data=s.recvfrom(1000)
		print "data from client : ",data[0]
		print "ip of client is : ",data[1][0]
		
		p=raw_input("enter reply msg : ")
		s.sendto(p,data[1])

thread.start_new_thread(recv,())

while True:
	pass
