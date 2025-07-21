import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# AES key & IV file paths
KEY_FILE = 'aes_key.bin'
IV_FILE = 'aes_iv.bin'
RSA_ENCRYPTED_AES_KEY_FILE = 'encrypted_aes_key.bin'

# Generate and save AES key, IV, and encrypt AES key with RSA
def generate_key_iv():
    key = os.urandom(32)  # 256-bit AES key
    iv = os.urandom(16)   # 128-bit IV

    with open(KEY_FILE, 'wb') as kf:
        kf.write(key)
    with open(IV_FILE, 'wb') as ivf:
        ivf.write(iv)

    encrypt_aes_key_with_rsa(key)
    return key, iv

# Load AES key and IV (or generate if not found)
def load_key_iv():
    if not os.path.exists(KEY_FILE) or not os.path.exists(IV_FILE):
        return generate_key_iv()

    with open(KEY_FILE, 'rb') as kf:
        key = kf.read()
    with open(IV_FILE, 'rb') as ivf:
        iv = ivf.read()
    return key, iv

# AES Encryption
def encrypt(data):
    key, iv = load_key_iv()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

# AES Decryption
def decrypt(encrypted_data):
    key, iv = load_key_iv()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_data) + decryptor.finalize()

# RSA Encryption of AES Key
def encrypt_aes_key_with_rsa(aes_key):
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(RSA_ENCRYPTED_AES_KEY_FILE, "wb") as f:
        f.write(encrypted_key)

    print("✅ AES key encrypted with RSA and saved to encrypted_aes_key.bin")
