import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP range.')
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    # Get documentation of the class fields
    # scapy.ls(scapy.ARP())
    # the destination mac address is a virtual address where all devices will receive
    # the src is the device mac address by default
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    # Scapy overloads the / operator to allow packet combination
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)

    for element in answered:
        print(element[1].psrc)  # index 1 will be the packet sent
        print(element[1].hwsrc)  # index 1 will be the packet sent


scan('192.168.65.1/24')
