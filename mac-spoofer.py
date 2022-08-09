import subprocess
import string
import random
import time
import re

iface = 'eth0'
output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
current_mac = (re.search("ether (.+) ", output).group().split()[1].strip()).upper()
	

def generate_random_mac_addr():
	global mac_addr

	uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
	
	mac_addr = ''
	
	for mac in range(6):
		for block in range(2):
			if mac == 0:
				mac_addr += random.choice('02468ACE')
			else:
				mac_addr += random.choice(uppercased_hexdigits)
				
		mac_addr += ':'
	
	mac_addr = mac_addr.strip(':')

	
def change_mac_addr(iface, mac_addr):
	subprocess.check_output(f'ifconfig {iface} down', shell=True)
	subprocess.check_output(f'ifconfig {iface} hw ether {mac_addr}', shell=True)
	subprocess.check_output(f'ifconfig {iface} up', shell=True)
	
	
if __name__ == '__main__':
	print(f"Your cuurent MAC Address: {current_mac}")

	while True:
		generate_random_mac_addr()
		change_mac_addr(iface, mac_addr)
		print(f"[!] MAC Successfully Changed To: {mac_addr}")
		time.sleep(600)
