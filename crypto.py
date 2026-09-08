"""
Project: Kurosh Cypher - Specter Pipe Crypto Engine
Description: End-to-end encryption module for payload fragmentation and security.
Environment: Termux / Python 3.x
"""

import base64
import hashlib

def simple_encrypt(clear_text, secret_key):
    """A lightweight XOR and Base64 cryptographic obfuscation layer for payload transmission."""
    key_hash = hashlib.sha256(secret_key.encode()).digest()
    encrypted_chars = []
    
    for i, char in enumerate(clear_text):
        key_char = key_hash[i % len(key_hash)]
        encrypted_char = ord(char) ^ key_char
        encrypted_chars.append(encrypted_char)
        
    encoded_payload = base64.b64encode(bytes(encrypted_chars)).decode('utf-8')
    return encoded_payload

def simple_decrypt(encoded_payload, secret_key):
    """Decrypts the received payload back to clear text using the shared secret key."""
    try:
        key_hash = hashlib.sha256(secret_key.encode()).digest()
        decoded_bytes = base64.b64decode(encoded_payload.encode('utf-8'))
        
        decrypted_chars = []
        for i, byte in enumerate(decoded_bytes):
            key_char = key_hash[i % len(key_hash)]
            decrypted_char = chr(byte ^ key_char)
            decrypted_chars.append(decrypted_char)
            
        return "".join(decrypted_chars)
    except Exception as e:
        return f"[-] Decryption failed: {e}"

if __name__ == "__main__":
    # تست ماژول رمزنگاری
    secret = "KuroshSecretPass2026"
    message = "SPECTER_PIPE: Secure encrypted transmission test."
    
    encrypted = simple_encrypt(message, secret)
    print(f"[+] Encrypted Payload: {encrypted}")
    
    decrypted = simple_decrypt(encrypted, secret)
    print(f"[+] Decrypted Message: {decrypted}")
          
