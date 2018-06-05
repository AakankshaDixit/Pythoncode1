
#!/usr/bin/python

import  socket,time 
import thread

import pyttsx
engine = pyttsx.init()

rec_ip="192.168.43.102"
myport=9999
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 
t=time.time()+10

while 4>2:
	
	msg=s.recvfrom(1000)
	engine.say(msg[0])
	engine.say("   ")
	engine.runAndWait()
	p=raw_input("enter reply msg :")
	s.sendto(p,msg[1])




