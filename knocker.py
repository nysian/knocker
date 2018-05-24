#!/usr/bin/env python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# created by P. Renee Carnley for CSC 842 Green Team Cycle 2  #
# Knocker is a port scanning tool for websites                #
# ****DISCLAIMER - author is not responsible for illegal use  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import signal
import socket
import subprocess
import sys
import time
import urllib

website = sys.argv[1]
numOpen = 0
numClosed = 0
try:
    server = socket.gethostbyname(website)

    print 'knocking on ' + website + ' at ip: ' + server

    for port in range(1, 100):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        knock = soc.connect_ex((server, port))
        print "Port {}: ".format(port),
        if knock == 0:
            print "open"
            numOpen += 1
        else:
            print "closed"
            numClosed += 1
        soc.close()

except socket.gaierror, msg:
    print 'Website name failed '
    sys.exit()
except socket.error:
    print 'Could not connect to website'
    sys.exit()
except socket.timeout:
    print 'Connection timed out'
except KeyboardInterrupt:
    sys.exit()

print 'Number of open ports {} Number of closed ports {}'.format(numOpen, numClosed)
