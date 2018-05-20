#!/usr/bin/python

import  socket,time 
from collections import Counter
import matplotlib.pyplot as plt
rec_ip="192.168.43.102"
myport=9999
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 
list=[]
t=time.time()+10
while time.time()<t:

	data=s.recvfrom(1000)
	#print "data from client : ",data[0]
	#print "ip of client is : ",data[1][0]
	list.append(data[0])
	print list	

	#p=raw_input("enter reply msg : ")
	#s.sendto(p,data[1])

count_v= Counter(list)
values= count_v.values()
keys = count_v.keys()
print "values are : ",type(values)
print "keys are : ", type(keys)

plt.bar(keys,values,color='r')
plt.grid(True,color='b')
plt.show()

