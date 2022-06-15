import socket #for ip of host machine
import whois #whois
import platform #ping
import subprocess #ping

def ping(host):
    #Returns True if host (str) responds to a ping request.

    para = '-n' if platform.system().lower()== 'windows' else '-c' #setting the paramater in accordance with the OS

    # Building the command. Ex: "ping -c 1 google.com"
    comm = ['ping', para, '1', host]
    print ("\n\nPing::" + host)
    return subprocess.call(comm) == 0

def whoiss(host):
    w = whois.whois(host)  # getting whois information
    print("\nWhois::"+host)
    print(w)

hostname = socket.gethostname() #getting the hostname by socket.gethostname() method that is host machine
hostname2 = "www.google.com"
ip_address = socket.gethostbyname(hostname2) #getting the IP address using socket.gethostbyname() method


## printing IP and hostname
print(f"\nHostname: {hostname2}")
print(f"IP Address: {ip_address}\n")

whoiss(hostname2)
ping(hostname2)