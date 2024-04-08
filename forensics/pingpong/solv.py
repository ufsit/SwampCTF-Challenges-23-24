#!/bin/python3
from scapy.all import *
from base64 import b64decode

p = rdpcap('traffic.pcap')

s = [i.load for i in p if i.haslayer(ICMP)]

base64data = b''.join(s)

imagedata = b64decode(base64data)

with open('flag.png', 'wb') as fout:
	fout.write(imagedata)
