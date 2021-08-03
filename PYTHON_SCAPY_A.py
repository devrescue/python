from scapy.all import *

#pip install --pre scapy[complete]

packet = rdpcap('datasets/http.cap')

print(packet)

p = packet[0] #first packet in the capture
p.show()


p = packet[3] #fourth packet in the capture
p.show()

p[TCP].dport = 8080
p.show()

p[TCP].dport = 8045
p.show()

p = IP()/TCP() #create a new packet
p.show()

p[TCP].dport = 35
p.show()

p = IP(dst='8.8.8.8')/TCP(dport=53) #create a new packet
p.show()
