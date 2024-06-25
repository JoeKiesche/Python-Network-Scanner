import pyfiglet
import sys
from scapy.all import ICMP, IP, sr1
from netaddr import IPNetwork
import socket
import datetime 

from pyfiglet import Figlet

#Create cool logo
def printLogo():
    logo = pyfiglet.figlet_format("Port Scanner" ,font= 'slant')
    print(logo)

#   Gets the host IP of the local machine
def getLocalHost():
    Localhost = socket.gethostname()
    ipaddr = socket.gethostbyname(Localhost)
    return ipaddr


def enterNetmask():
    mask = input("Enter in the desired netmask: ")
    return mask

#   Lets user choose the host they want to scan
def enterHost():
    host = input("Enter in the desired target: ")
    return host 

def ping_sweep(network, netmask):
    live_hosts = []
    total_hosts = 0
    scanned_hosts = 0

    ip_network = IPNetwork(network + '/' + netmask)
    for host in ip_network.iter_hosts():
        total_hosts += 1

    for host in ip_network.iter_hosts():
        scanned_hosts += 1
        print(f"Scanning: {scanned_hosts}/{total_hosts}", end="\r")
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is not None:
            live_hosts.append(str(host))
            print(f"Host {host} is online.")

    return live_hosts 

if __name__ == "__main__":
    printLogo()
    print("[1]  Enter in a host IP")
    print("[2]  Use the local IP address of this machine")
    print("[3]  Exit")
    choice = input("Enter in a choice")

    if choice == "1":
        network = enterHost()
        netmask = enterNetmask()
    else:
        network = getLocalHost()
        netmask = enterNetmask()



    live_hosts = ping_sweep(network, netmask)
    print("Completed\n")
    print(f"live hosts: {live_hosts}")