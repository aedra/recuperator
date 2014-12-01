import serial
from datetime import datetime, date, time

port = serial.Serial("/dev/ttyAMA0", baudrate=2400, timeout=1.0)

fo = open("output-raw.txt","w")

# block read
while True:
	rcv = ord(port.read(1))
	cd = datetime.now()
	print >>fo, cd ,rcv
#	print rcv
fo.close()