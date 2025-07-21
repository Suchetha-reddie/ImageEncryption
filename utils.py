from PIL import Image
import numpy as np

def image_to_bytes(image_path):
    """
    Converts an image to raw byte data and returns its size.
    """
    img = Image.open(image_path).convert("RGB")   # Ensure 3 channels
    img_array = np.array(img)
    return img_array.tobytes(), img.size          # Returns (bytes, (width, height))

def bytes_to_image(byte_data, size, output_path):
    """
    Converts byte data back to an image and saves it.
    """
    img_array = np.frombuffer(byte_data, dtype=np.uint8)
    img_array = img_array.reshape((size[1], size[0], 3))  # height, width, channels
    img = Image.fromarray(img_array)
    img.save(output_path)