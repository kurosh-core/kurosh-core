"""
Project: Kurosh Cypher - Specter Pipe Interactive CLI
Description: Interactive command-line interface to manage nodes, encryption, and sending payloads.
Environment: Termux / Python 3.x
"""

import sys
import threading
from engine import SpecterEngine
from client import send_payload
from node import start_node

def print_banner():
    print("========================================")
    print("   SPECTER PIPE - SECURE MESH CLI       ")
    print("   Persona: Kurosh Cypher               ")
    print("========================================")
    print("1. Start P2P Listener Node")
    print("2. Send Encrypted Fragmented Payload")
    print("3. Exit")
    print("========================================")

def interactive_cli():
    secret_key = "KuroshSecretPass2026"
    engine = SpecterEngine(secret_key)
    
    while True:
        print_banner()
        choice = input("Select an option [1-3]: ").strip()
        
        if choice == "1":
            port = input("Enter port to listen on (default 5000): ").strip()
            port = int(port) if port.isdigit() else 5000
            print(f"[*] Starting background listener node on port {port}...")
            
            # اجرای نود در یک ترد جداگانه تا خط فرمان مسدود نشود
            node_thread = threading.Thread(target=start_node, args=('0.0.0.0', port), daemon=True)
            node_thread.start()
            print("[+] Listener active in background. Press Enter to continue...")
            input()
            
        elif choice == "2":
            target_ip = input("Enter target peer IP (e.g., 127.0.0.1): ").strip() or "127.0.0.1"
            port_input = input("Enter target peer Port (default 5000): ").strip()
            target_port = int(port_input) if port_input.isdigit() else 5000
            
            message = input("Enter message to transmit securely: ").strip()
            if not message:
                message = "Default Specter Pipeline Message."
                
            print("[*] Preparing encrypted fragments...")
            packets = engine.prepare_packet(message, chunk_size=25)
            
            print(f"[*] Sending {len(packets)} fragments to {target_ip}:{target_port}...")
            for pkt in packets:
                send_payload(target_ip, target_port, pkt)
                
            print("[+] All packets dispatched successfully.")
            input("\nPress Enter to return to menu...")
            
        elif choice == "3":
            print("[*] Exiting Specter Pipe CLI. Stay secure.")
            sys.exit(0)
        else:
            print("[-] Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    try:
        interactive_cli()
    except KeyboardInterrupt:
        print("\n[*] Interrupted. Shutting down safely.")
          
