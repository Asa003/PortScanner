#!/bin/python3
import sys
import socket
from datetime import datetime


#Target
if len(sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("Invalid Parameter Syntax")
	print("Syntax : python3 s3.py <IP/HOSTNAME>")


#Banner
print("\033[32m-"*50)
print("Author: Swayam")
print("Scanning target: "+str(target))
print("Time started: "+str(datetime.now()))
print("-"*50)
print("\033[0m")


#Connection
try:
	for port in range(79,445):
		#print(port) //for troubleshooting purpose
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		socket.setdefaulttimeout(0.3)
		result=s.connect_ex((target,port))
		if result==0:
			print("Port {} is open".format(port))
		s.close()
		
		
#Exceptions	
except KeyboardInterrupt:
	print("\n")
	print("Exiting Program")
	sys.exit()	

				
