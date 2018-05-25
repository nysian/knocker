#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# created by P. Renee Carnley for CSC 842 Green Team Cycle 2  #
# Knocker is a port scanning tool for websites                #
# ****DISCLAIMER - author is not responsible for illegal use  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import random
import signal
import socket
import subprocess
import sys
import time
import threading
import urllib
import webbrowser

#Check if user ran with a website
if len(sys.argv) > 1:
    website = sys.argv[1] #set variable website to user defined website
else:
    print ('Must enter a website when running. ex: py knocker.py somewebsite.com')
    sys.exit()

#check if random is desired
if len(sys.argv) > 2:
    randomizer = int(sys.argv[2])
else:
    randomizer = 0

#check if user defined a setdefaulttimeout
if len(sys.argv) > 3:
    timeout = float(sys.argv[3]) #set variable timeout to user defined timeout period
else:
    timeout = 3

#Check if user defined number of ports to knock
if len(sys.argv) > 4:
    numports = int(sys.argv[4]) #set variable numports to user defined number of ports
else:
    numports = 65536


#initialize variables for counting number of open and closed ports
numOpen = 0
numClosed = 0

#initialize total possible numports
totalports = 65535

#check for open ports
try:
    server = socket.gethostbyname(website) #get the IP address of the website

    print ('knocking on ' + website + ' at ip: ' + server)
    #knock on ports
    for i in range(1, numports):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout)

        if randomizer == 1:
            port = i;
        else:
            #randomly get a port number within range
            port = random.randint(1,totalports)

        knock = soc.connect_ex((server, port))
        print ("Port {}: ".format(port), end="")

        #check if port is opened
        if knock == 0:
            print ("open")
            numOpen += 1
        else:
            print ("closed")
            numClosed += 1
        soc.close()

#catch if bad website name
except socket.gaierror:
    print ('Website name failed ')
    sys.exit()

#catch if no connection to website could be made
except socket.error:
    print ('Could not connect to website')
    sys.exit()

#catch if connection timed out
except socket.timeout:
    print ('Connection timed out')

#catch if user wants to stop
except KeyboardInterrupt:
    print('User Interrupt....shutting down')
    soc.close() #ensure socket is closed before exiting
    sys.exit()

print ('Number of open ports {} Number of closed ports {}'.format(numOpen, numClosed))
webbrowser.open(website)
