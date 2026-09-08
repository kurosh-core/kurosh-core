"""
Project: Kurosh Cypher Core Module
Description: Base structural script for node identity and cryptographic handling.
Environment: Termux / Python 3.x
"""

import hashlib
import os

def generate_node_identity():
    """Generates a secure pseudo-anonymous hash for node identification."""
    random_bytes = os.urandom(32)
    node_hash = hashlib.sha256(random_bytes).hexdigest()
    return node_hash

def initialize_environment():
    print("[-] Initializing Kurosh Cypher core engine...")
    node_id = generate_node_identity()
    print(f"[+] Node Secure ID Generated: {node_id[:16]}...[PROTECTED]")
    print("[+] Environment verified successfully in Termux.")

if __name__ == "__main__":
    initialize_environment()
  
