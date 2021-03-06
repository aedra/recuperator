import serial
from datetime import datetime, date, time
import time

def check_checksum(tl):
	ss = sum(tl[0:6]) & 0xFF
	return (((~ss) & 0xFF)+1)&0xFF

def tx_packet(tvalues):
	for val in tvalues:
		port.write(chr((~val)&0xFF))


idx = 0
arr = ['0']		# for file I/O handling
val = [0]		# for calculation
cks = 0
datestr = ['0']
tempRoom = [0]*8
tempSet = [0]*8
txarr = [181, 0, 7, 130, 1, 193]
# uart clock was adjusted from 3MHz to xxx to tweak the baud rate
# 4800bps has 5200bps in real measurement

port = serial.Serial("/dev/ttyAMA0", baudrate=2400, timeout=1.0)

fo = open("packetlog-recuperator.txt","w")
print >> fo, "Date", "Time", "Byte0", "Byte1", "Byte2", "Byte3", "Byte4", "Byte5", "Byte6"
cd = datetime.now()

while True:
# read 1byte from serial port and store it into packet array
	t0 = time.time()
	tbyte = port.read(1)
	rcv = str((~ord(tbyte))&0xFF)
	t1 = time.time()
	if t1-t0 > 0.05:
		cmdset = ' '.join(arr)
		print arr
		if len(arr) > 4:
			if arr[0]=='213':
				time.sleep(0.11)
				tx_packet(txarr)

		print >> fo, cd, cmdset

		# initialize variables
		idx = 0
		arr = ['0']
		arr[0] = rcv
		val = [0]
		val[0] = int(rcv)
		cd = datetime.now()
		# compare checksum
			# place command parsing and functions for each commands
	else:
		arr.append(rcv)
		val.append(int(rcv))

	idx +=1

fo.close()