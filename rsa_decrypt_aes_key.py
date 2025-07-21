from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Load the encrypted AES key
with open("encrypted_aes_key.bin", "rb") as f:
    encrypted_key = f.read()

# Load the private RSA key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Decrypt the AES key
decrypted_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save decrypted AES key (for testing)
with open("decrypted_aes_key.bin", "wb") as f:
    f.write(decrypted_key)

print("✅ AES key successfully decrypted from RSA!")
