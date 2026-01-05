import cv2
import numpy as np
from PIL import Image
import io

def bytes_to_image(file_bytes) -> np.ndarray:
    """Convert uploaded file bytes to OpenCV image"""
    nparr = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image

def image_to_bytes(image: np.ndarray, format: str = "JPEG") -> bytes:
    """Convert OpenCV image to bytes"""
    # Convert BGR to RGB for PIL
    if len(image.shape) == 3:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        image_rgb = image

    pil_image = Image.fromarray(image_rgb)
    img_byte_arr = io.BytesIO()
    pil_image.save(img_byte_arr, format = format)
    return img_byte_arr.getvalue()

def resize_image(image: np.ndarray, max_size: tuple = (800, 800)) -> np.ndarray:
    """Resize image while maintaining aspect ratio"""
    height, width = image.shape[:2]

    if height > max_size[0] or width > max_size[1]:
        scale = min(max_size[0] / height, max_size[1] / width)
        new_width = int(width * scale)
        new_height = int(height * scale)

        image = cv2.resize(image, (new_width, new_height), interpolation = cv2.INTER_AREA)

    return image