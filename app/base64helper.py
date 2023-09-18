import os
import base64
from PIL import Image
import io

# Function to compress and convert an image to base64

def compressimagefromfilepath(file_path):
    try:
        # Opens the image using Pillow
        with Image.open(file_path) as img:
            # Compresses the image
            img = img.convert("RGB")  # Convert to RGB if it's not

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=30)
            img_data = img_io.getvalue()

            # Converts to base64
            base64_encoded = base64.b64encode(img_data).decode('utf-8')
            return base64_encoded
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None
    
    
def compressimagefrombase64(base64_image):
    try:
        # Decode the base64 image data
        image_data = base64.b64decode(base64_image)

        # Opens the image using Pillow
        with Image.open(io.BytesIO(image_data)) as img:
            # Compresses the image
            img = img.convert("RGB")
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=30)
            compressed_image_data = img_io.getvalue()

            # Converts the compressed image back to base64
            compressed_base64 = base64.b64encode(compressed_image_data).decode('utf-8')
            return compressed_base64
    except Exception as e:
        print(f"Error compressing image: {str(e)}")
        return None
