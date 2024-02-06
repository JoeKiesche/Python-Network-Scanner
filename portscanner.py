import pyfiglet
import sys
import socket
import datetime 

from pyfiglet import Figlet
def printLogo():
    logo = pyfiglet.figlet_format("Port Scanner" ,font= 'slant')
    print(logo)

#   Gets the host IP of the local machine
def getLocalHost():
    host = socket.gethostname()
    return host

#   Lets user choose the host they want to scan
def enterHost():
    host = input("Enter in the desired target: ")
    return host 



#   Checks if port is open or closed
def scan(host):
    print("starting scan on ", host)
    print("\n")
    for port in range(134,446):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        res = s.connect_ex((host, port))
        if res == 0:
            print(f"on {host} port: {port} is Open")
        print("Scan has been finshed")
        s.close()

#   Displays a menu for the user
def displayMenu():
    print("Use the local machines ip: 1")
    print("enter in a target: 2")

        

def main():
    host = 1
    printLogo()
    while True:
        displayMenu()
        choice = input("please chooce an option: ")
        if choice == "1":
            host = getLocalHost()
            scan(host)
            break
        if choice == "2":
            host = enterHost()
            scan(host)
            break
        else:
            print("thats not an option!\n")

if __name__== "__main__":
    main()