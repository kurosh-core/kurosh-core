"""
Project: Kurosh Cypher - Specter Pipe Client Module
Description: Sends raw or fragmented payloads to peer nodes over TCP sockets.
Environment: Termux / Python 3.x
"""

import socket

def send_payload(target_ip, target_port, payload):
    """Sends a payload string to a target IP and port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((target_ip, target_port))
            s.sendall(payload.encode('utf-8'))
            return True
    except Exception as e:
        print(f"[-] Transmission error to {target_ip}:{target_port}: {e}")
        return False

if __name__ == "__main__":
    print("[*] Client module ready for dispatching payloads.")
      
