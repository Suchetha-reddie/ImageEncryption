from utils import image_to_bytes, bytes_to_image
from encryptor import encrypt, decrypt

# Step 1: Load image and convert to bytes
data, size = image_to_bytes('test_image.jpg.jpeg')

# Step 2: Encrypt the byte data
encrypted = encrypt(data)

# Step 3: Save encrypted data (optional)
with open('encrypted_image.dat', 'wb') as f:
    f.write(encrypted)

# Step 4: Decrypt the byte data
decrypted = decrypt(encrypted)

# Step 5: Save the decrypted image
bytes_to_image(decrypted, size, 'decrypted_image.jpg')

print("✅ Image encrypted and decrypted successfully.")
