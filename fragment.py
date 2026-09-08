"""
Project: Kurosh Cypher - Specter Pipe Fragmentation Module
Description: Splits payloads into smaller indexed chunks for mesh routing and reassembles them.
Environment: Termux / Python 3.x
"""

import math
import json
import uuid

def fragment_payload(payload, chunk_size=64):
    """Splits a payload string into smaller indexed fragments with metadata."""
    packet_id = str(uuid.uuid4())[:8]
    total_length = len(payload)
    total_chunks = math.ceil(total_length / chunk_size)
    
    fragments = []
    for i in range(total_chunks):
        start = i * chunk_size
        end = start + chunk_size
        chunk_data = payload[start:end]
        
        packet = {
            "id": packet_id,
            "index": i + 1,
            "total": total_chunks,
            "data": chunk_data
        }
        fragments.append(json.dumps(packet))
        
    return fragments

class PacketAssembler:
    """Reassembles incoming fragments back into the original payload."""
    def __init__(self):
        self.buffers = {}

    def add_fragment(self, packet_json):
        """Adds a packet chunk and returns the full payload if all chunks are received."""
        try:
            packet = json.loads(packet_json)
            packet_id = packet["id"]
            index = packet["index"]
            total = packet["total"]
            data = packet["data"]
            
            if packet_id not in self.buffers:
                self.buffers[packet_id] = {"total": total, "chunks": {}}
                
            self.buffers[packet_id]["chunks"][index] = data
            
            # بررسی اینکه آیا تمام تکه‌ها دریافت شده‌اند یا خیر
            if len(self.buffers[packet_id]["chunks"]) == total:
                complete_payload = "".join(
                    [self.buffers[packet_id]["chunks"][i] for i in range(1, total + 1)]
                )
                del self.buffers[packet_id]
                return complete_payload
                
        except Exception as e:
            print(f"[-] Assembly error: {e}")
            
        return None

if __name__ == "__main__":
    test_message = "SPECTER_PIPE: This is a long message that needs to be fragmented across the decentralized mesh network safely."
    print(f"[*] Original Message: {test_message}")
    
    chunks = fragment_payload(test_message, chunk_size=30)
    print(f"[+] Generated {len(chunks)} fragments.")
    
    assembler = PacketAssembler()
    reassembled = None
    
    for chunk in chunks:
        result = assembler.add_fragment(chunk)
        if result:
            reassembled = result
            
    print(f"[+] Reassembled Message: {reassembled}")

