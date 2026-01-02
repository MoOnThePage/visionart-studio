import cv2
import numpy as np

from core.image_processor import BaseEffect

class CartoonEffect(BaseEffect):
    """Cartoon effect using edge detection and bilateral filter"""
    def __init__(self):
        super().__init__(
            name = "cartoon",
            description = "Transform photos into cartoon"
        )
        self.config = {
            "blur_size": 5,
            "edge_threshold": 9,
            "sigma_color": 300,
            "sigma_space": 300
        }

    def apply(self, image: np.ndarray, **kwargs) -> np.ndarray:
        # Update config with kwargs
        self.config.update(kwargs)

        # convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        # Apply median blur
        gray = cv2.medianBlur(gray, self.config["blur_size"])

        # Detect edges
        edges = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            self.config["edge_threshold"],
            self.config["edge_threshold"]
        )

        # Apply bilateral for cartoon effect
        if len(image.shape) == 3:
            color = cv2.bilateralFilter(
                image,
                self.config["blur_size"],
                self.config["sigma_color"],
                self.config["sigma_space"]
            )
            # Combine edges with color
            cartoon = cv2.bitwise_and(color, color, mask=edges)
            return cartoon
        else:
            # For grayscale image
            return edges