🚀 Advanced Network Port Scanner (Multithreaded)
This is a high-performance Python-based Network Security tool developed to identify open ports and active services on a target host. This project explores the fundamentals of Socket Programming and enhances execution speed through Multithreading.

🛠️ Key Features
TCP Handshake Logic: Uses the standard TCP Three-Way Handshake to accurately detect open ports.

High-Speed Scanning: Implemented Multithreading to scan 1000+ ports in just a few seconds (significantly faster than single-threaded scanners).

Dynamic User Input: Allows the user to specify any Target IP or Hostname at runtime.

Real-time Logging: Displays timestamps for the start of each scan and provides instant feedback on discovered ports.

💻 Technical Stack
Language: Python 3.x

Modules Used:

socket: For low-level network connectivity.

threading: To manage concurrent execution and improve performance.

datetime: For precise session logging.

🚀 How to Run
Ensure you have Python installed on your system.

Clone this repository or download scanner.py.

Run the script using the following command:

Bash
python3 scanner.py
Enter the target IP address (e.g., 127.0.0.1 for local testing).

📊 Sample Output
Plaintext
Scanning Target: 10.112.176.35
Scanning started at: 2026-03-23 13:27:13
--------------------------------------------------
[*] Initializing Multithreaded Scan... Please wait.
[+] Port 53: OPEN
