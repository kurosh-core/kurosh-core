"""
Project: Kurosh Cypher - Specter Pipe Sender Module
Description: Client script to transmit fragmented/encrypted payloads to peer nodes.
Environment: Termux / Python 3.x
"""

import socket
import sys

def send_payload(target_ip, target_port, message):
    """Connects to a target peer node and transmits the payload securely."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"[*] Connecting to peer node {target_ip}:{target_port}...")
        client.connect((target_ip, target_port))
        
        # ارسال پیام رمزنگاری‌شده یا داده
        print(f"[*] Transmitting payload: {message}")
        client.sendall(message.encode('utf-8'))
        
        # دریافت پاسخ تاییدیه از نود مقابل
        response = client.recv(1024)
        print(f"[+] Response from peer: {response.decode('utf-8')}")
        
    except ConnectionRefusedError:
        print(f"[-] Connection failed: Target node {target_ip}:{target_port} is offline or unreachable.")
    except Exception as e:
        print(f"[-] Transmission error: {e}")
    finally:
        client.close()
        print("[*] Connection closed.")

if __name__ == "__main__":
    # به صورت پیش‌فرض به لوکال هاست (خودِ سیستم) وصل می‌شود برای تست
    HOST = '127.0.0.1'
    PORT = 5000
    
    payload = "SPECTER_PAYLOAD: Test secure fragmented data packet."
    
    send_payload(HOST, PORT, payload)
      
