import cv2
import numpy as np
from core.image_processor import BaseEffect
from main import width


class UpscalerEffect(BaseEffect):
    """Image upscaling with interpolation"""

    def __init__(self):
        super().__init__(
            name = "upscale",
            description = "Image 2X upscaling with interpolation"
        )
        self.config = {
            "scale_factor": 2,
            "interpolation": cv2.INTER_CUBIC
        }

    def apply(self, image: np.ndarray, **kwargs) -> np.ndarray:
        self.config.update(kwargs)

        height, width = image.shape[:2]
        new_height = int(width * self.config["scale_factor"])
        new_width = int(new_height * self.config["scale_factor"])

        # Resize the image
        upscaled = cv2.resize(
            image,
            (new_width, new_height),
            interpolation = self.config["interpolation"]
        )

        return upscaled

