from scapy.all import *

TIMEOUT = 2
conf.verb = 0
for ip in range(0, 10):
    packet = IP(dst="192.168.0." + str(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
         print(reply.dst, "is online")
    else:
         print(f"Timeout waiting for {packet[IP].dst}")
