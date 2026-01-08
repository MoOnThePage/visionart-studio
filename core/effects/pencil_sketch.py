import cv2
import numpy as np
from core.image_processor import BaseEffect
# from main import inverted_blurred


class PencilSketchEffect(BaseEffect):
    """Pencil sketch effect using inversion and division"""
    def __init__(self):
        super().__init__(
            name = "pencil_sketch",
            description = "Convert to pencil sketch"
        )
        self.config = {
            "blur_kernel": (21, 21),
            "scale": 256.0
        }

    def apply(self, image: np.ndarray, **kwargs) -> np.ndarray:
        self.config.update(kwargs)

        # convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        # Invert and blur
        inverted = cv2.bitwise_not(gray)
        blurred = cv2.GaussianBlur(inverted, self.config["blur_kernel"], 0)
        inverted_blurred = cv2.bitwise_not(blurred)

        # Create sketch
        sketch = cv2.divide(gray, inverted_blurred, scale = self.config["scale"])

        # Convert back to 3-channel if needed
        if len(image.shape) == 3:
            sketch = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

        return sketch