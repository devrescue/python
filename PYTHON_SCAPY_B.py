from scapy.all import *

ports = [25,80,53,443,445,8080,8443]

def SynScan(host): #sends syn packets to each port, track responses
    ans, unans = sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags="S"),timeout=2,verbose=0) #ans and unanswered packets
    print(f"Open ports at {host}")
    for(s,r) in ans: #looping over collection of answer packets, verifying that we got response from the port we sent the packet to
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport)


def DNSScan(host): #connect to a particular port on a  particular host and see if it properly responds to a DNS request
    ans, unans = sr(IP(dst=host)/UDP(sport=5555,dport=53)/DNS(rd=1,qd=DNSQR(qname='google.com')),timeout=2,verbose=0)
    if ans:
        print(f"DNS Server at {host}")

host = "8.8.8.8"

SynScan(host)
DNSScan(host)

