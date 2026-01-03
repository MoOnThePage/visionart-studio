import cv2
import numpy as np

from core.image_processor import BaseEffect

class OilPaintingEffect(BaseEffect):
    """Create an oil painting effect."""
    def __init__(self):
        super().__init__(
            name = "oil_painting",
            description = "Create oil painting effect"
        )
        self.config = {
            "size": 7,
            "dynRation": 1
        }

    def apply(self, image: np.ndarray, **kwargs) -> np.ndarray:
        self.config.update(kwargs)

        # convert to BGR if Grayscale
        if (len(image.shape) == 2):
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        # Apply oil painting effect
        result = cv2.xphoto.oilPainting(
            image,
            self.config["size"],
            self.config["dynRation"],
        )

        return result