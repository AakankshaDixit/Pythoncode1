#!/usr/bin/python3
import time
import webbrowser
import requests
from bs4 import BeautifulSoup

option='''
Press 1: to enter any thing - split each word and search on google
Press 2: same but find url
Press 3: same but find images answer
Press 4: current time and date
Press 5: open default browser
Press 6: all network IP
Press 7: enter domain name and find owner,email,contact
'''
print(option)

ch=input()

if ch == '1' :
	search_data = input("enter the data:")
	final_data=search_data.strip()
	# above removing leading and trailing space
	done_data=final_data.split()
	#Splitting each word by space

	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)
 
else : 
	print ( "no chance!!")

if ch == '2' :
	data=input("enter the data")
	find_url = data.strip()
	final_1 = find_url.split()
	print(final_1)
	#Scrapping the data to extract the urls
	for i in final_1:
		r=requests.get('https://www.google.com/search?q='+i)
		data=r.content
		soup= BeautifulSoup(data,'html.parser')
		
		for link in soup.find_all('a'):
			print(link.get('href'))
		
else:

	print("sorry!!")

	      
