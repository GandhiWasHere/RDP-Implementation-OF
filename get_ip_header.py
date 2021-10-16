from scapy.all import sr1
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
def retrive_windowsize_rdp(ip):
    return sr1(IP(dst=ip) / TCP(dport=[3389]), verbose=0, timeout=3)[1].window