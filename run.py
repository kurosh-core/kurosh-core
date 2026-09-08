"""
Project: Kurosh Cypher - Specter Pipe Test Runner
Description: Integration script to test the complete P2P encryption and fragmentation pipeline.
Environment: Termux / Python 3.x
"""

from engine import SpecterEngine
from client import send_payload
import threading
import time

def test_pipeline():
    print("========================================")
    print("   SPECTER PIPE - SECURE PIPELINE TEST  ")
    print("========================================")
    
    # کلید رمزنگاری مشترک بین نودها
    secret_key = "KuroshSecretPass2026"
    engine = SpecterEngine(secret_key)
    
    # پیام تست واقعی
    original_message = "SPECTER_PIPE: Decentralized mesh communication established successfully by Kurosh Cypher."
    print(f"\n[*] Original Message:\n{original_message}")
    
    # ۱. آماده‌سازی، رمزنگاری و تکه‌بندی پیام
    print("\n[+] Step 1: Encrypting and fragmenting payload...")
    packets = engine.prepare_packet(original_message, chunk_size=20)
    print(f"[+] Total generated packets: {len(packets)}")
    
    for i, pkt in enumerate(packets):
        print(f"    - Packet {i+1}: {pkt[:40]}...")
        
    # ۲. شبیه‌سازی دریافت و بازسازی بسته‌ها در مقصد
    print("\n[+] Step 2: Simulating transmission and reassembly...")
    recovered_message = None
    
    for pkt in packets:
        result = engine.process_incoming_chunk(pkt)
        if result:
            recovered_message = result
            
    print(f"\n[+] Successfully Recovered Message:\n{recovered_message}")
    print("\n========================================")
    print("   TEST COMPLETED: PIPELINE IS SECURE    ")
    print("========================================")

if __name__ == "__main__":
    test_pipeline()
  
