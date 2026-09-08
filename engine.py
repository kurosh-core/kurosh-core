"""
Project: Kurosh Cypher - Specter Pipe Core Engine Integration
Description: Unifies encryption, fragmentation, and transmission workflow.
Environment: Termux / Python 3.x
"""

from crypto import simple_encrypt, simple_decrypt
from fragment import fragment_payload, PacketAssembler

class SpecterEngine:
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.assembler = PacketAssembler()

    def prepare_packet(self, raw_message, chunk_size=30):
        """Encrypts the message and splits it into secure fragments."""
        encrypted_data = simple_encrypt(raw_message, self.secret_key)
        fragments = fragment_payload(encrypted_data, chunk_size=chunk_size)
        return fragments

    def process_incoming_chunk(self, chunk_json):
        """Processes an incoming packet chunk, decrypts and reassembles if complete."""
        complete_encrypted = self.assembler.add_fragment(chunk_json)
        if complete_encrypted:
            original_message = simple_decrypt(complete_encrypted, self.secret_key)
            return original_message
        return None

if __name__ == "__main__":
    engine = SpecterEngine(secret_key="KuroshSecretPass2026")
    
    msg = "SPECTER_PIPE: Full pipeline test integrating crypto and fragmentation layers."
    print(f"[*] Original Message: {msg}")
    
    # آماده‌سازی و رمزنگاری/تکه‌بندی بسته‌ها
    packets = engine.prepare_packet(msg, chunk_size=25)
    print(f"[+] Prepared {len(packets)} encrypted packets.")
    
    # شبیه‌سازی دریافت و بازسازی در مقصد
    recovered_msg = None
    for pkt in packets:
        res = engine.process_incoming_chunk(pkt)
        if res:
            recovered_msg = res
            
    print(f"[+] Recovered Message: {recovered_msg}")
          
