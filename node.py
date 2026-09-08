"""
Project: Kurosh Cypher - Specter Pipe P2P Node
Description: Core peer-to-peer socket communication engine.
Environment: Termux / Python 3.x
"""

import socket
import threading

def handle_peer(client_socket, address):
    """Handles incoming data stream from a connected peer node."""
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"\n[+] Received encrypted payload from {address}: {message}")
            
            # ارسال پاسخ تایید دریافت به نود مقابل
            client_socket.send("ACK: Packet received securely.".encode('utf-8'))
    except Exception as e:
        print(f"[-] Connection error with {address}: {e}")
    finally:
            client_socket.close()

def start_node(host='0.0.0.0', port=5000):
    """Starts the P2P node listener on the local interface."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((host, port))
        server.listen(5)
        print(f"[*] Kurosh Cypher P2P Node active on {host}:{port}")
        print("[*] Listening for decentralized mesh traffic...")
        
        while True:
            client_socket, addr = server.accept()
            print(f"[+] Established secure link with peer: {addr[0]}:{addr[1]}")
            
            # ایجاد ترد مستقل برای هر نود متصل شده
            peer_thread = threading.Thread(target=handle_peer, args=(client_socket, addr))
            peer_thread.start()
            
    except Exception as e:
        print(f"[-] Node binding failed: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    # راه‌اندازی نود روی پورت محلی
    start_node()
    
