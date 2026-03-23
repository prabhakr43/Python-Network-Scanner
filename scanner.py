import socket
import threading
from datetime import datetime

# Step 1: Request Target IP from the user
# Use 127.0.0.1 (Localhost) to test it on your own machine
target_ip = input("Enter the Target IP address to scan: ")

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

def scan_port(port):
    """
    Function to check if a specific TCP port is open.
    Uses the TCP Three-Way Handshake logic (SYN/ACK).
    """
    try:
        # Create a socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a 1-second timeout to handle filtered or slow ports
        s.settimeout(1)
        
        # connect_ex returns 0 if the port is open and reachable
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        
        # Always close the connection to free up system resources
        s.close()
    except Exception:
        # Silently catch errors from closed or blocked ports
        pass

# Step 2: Implementing Multithreading for High-Speed Scanning
# This loop scans standard ports (1 to 1024) simultaneously
print("[*] Initializing Multithreaded Scan... Please wait.")

for port in range(1, 1025):
    # Creating a dedicated thread for each port to speed up execution
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()