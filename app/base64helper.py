import os
import base64
from PIL import Image
import io


def compressimagefromfilepath(file_path):
    """
    Compress an image file from the given file path.

    """
    try:
        with Image.open(file_path) as img:
            img = img.convert("RGB")
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=30)
            img_data = img_io.getvalue()
            base64_encoded = base64.b64encode(img_data).decode('utf-8')
            return base64_encoded
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None


def compressimagefrombase64(base64_image):
    """
    Compresses image from a base64-encoded string.
.
    """
    try:
        image_data = base64.b64decode(base64_image)
        with Image.open(io.BytesIO(image_data)) as img:
            img = img.convert("RGB")
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=30)
            compressed_image_data = img_io.getvalue()
            compressed_base64 = base64.b64encode(
                compressed_image_data).decode('utf-8')
            return compressed_base64
    except Exception as e:
        print(f"Error compressing image: {str(e)}")
        return None
