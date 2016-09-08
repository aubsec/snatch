import datetime
import os
import time

hostname = "w7el004144"

def PingLookup():
	while 1 == 1:
		print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		response = os.system("ping -n 1 " + hostname)
		if response == 0:
			SnatchFiles()
		else:
			time.sleep(300)
			continue

def SnatchFiles():
	try:
		snatch_files = os.system("robocopy /MIR /R:0 /W:0 \\\\" + hostname + "\\c$\\users\\ c:\\csirt-tools\\investigations\\  *")
		if snatch_files != 1:
			PingLookup()
		return 0
	except:
		PingLookup()
			
SnatchFiles()			
			
print("[!] Done!")
exit(0)