# verify_keys.py

# Open the original AES key
with open("aes_key.bin", "rb") as f1, open("decrypted_aes_key.bin", "rb") as f2:
    original = f1.read()
    decrypted = f2.read()

# Compare the two keys
if original == decrypted:
    print("✅ Decryption verified: AES key matches!")
else:
    print("❌ Decryption failed: Keys do not match.")
