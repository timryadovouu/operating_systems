from scapy.all import *
from netfilterqueue import NetfilterQueue
import os

os.system("sudo iptables -A INPUT -j NFQUEUE --queue-num 0")

def packet_callback(packet):
    ip_packet = IP(packet.get_payload())
    packet.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(0, packet_callback)

try:
    print("---packet filtering started---")
    nfqueue.run()
except KeyboardInterrupt:  # ctrl + c
    print("---packet filtering stopped---")
    nfqueue.unbind()