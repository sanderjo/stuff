import socket
import time
import sys

def send(command):
    totalcommand = command + "\r\n"
    print "Command sent is", totalcommand
    sslSocket.write(totalcommand)
    time.sleep(0.3)
    return sslSocket.read(5000)


###### MAIN

orig_timeout = socket.getdefaulttimeout()
socket.setdefaulttimeout(2.0)
print "Let's go"

if len(sys.argv) >= 2:
	newsserver = sys.argv[1]
else:
	newsserver = 'sslreader.eweka.nl'
	print "No newsserver specified, so using ... ", newsserver

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((newsserver, 563))
#s.connect((newsserver, 443))

sslSocket = socket.ssl(s)
welcomemsg = sslSocket.read(5000)   # Read the welcome message
print "Welcome is:", welcomemsg
if welcomemsg.find('200')>-1:
	print "Yes, found"

#print send("HELP")
#print send("LIST")

send("QUIT")

s.close()

