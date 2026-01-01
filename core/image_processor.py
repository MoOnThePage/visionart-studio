import cv2
import numpy as np
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import streamlit as st

class BaseEffect(ABC):
    """Base class for all effects."""

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.config = {}

    @abstractmethod
    def apply(self, image: np.ndarray, **kwargs) -> np.ndarray:
        """Apply the effect to the given image."""
        pass

    def validate_image(self, image: np.ndarray) -> bool:
        """Validate the given image."""
        if image is None:
            return False
        if len(image.shape) not in [2, 3]:
            return False
        return True

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """preprocess the given image."""
        return image.clip()

    def postprocess(self, image: np.ndarray) -> np.ndarray:
        """postprocess the given image."""
        return image

class ImageProcessor:
    """Base class for all image effects"""
    def __init__(self):
        self.effects: Dict[str, BaseEffect] = {}

    def register_effect(self, name:str, effect: BaseEffect):
        """Register an effect."""
        self.effects[name] = effect

    def get_effect(self, name: str) -> Optional[BaseEffect]:
        """Get the effect by name."""
        return self.effects.get(name)

    def list_effects(self) -> Dict[str, BaseEffect]:
        """List the available effects."""
        return self.effects

    def process(self, effect_name: str, image: np.ndarray, **kwargs) -> np.ndarray:
        """Apply the effect to the given image."""
        effect = self.get_effect(effect_name)
        if not effect:
            raise ValueError(f"Effect {effect_name} not found")

        if not effect.validate_image(image):
            raise ValueError(f"Invalid image {image}")

        # apply preprocessing
        processed = effect.preprocess(image)

        # apply main effect
        processed = effect.apply(processed, **kwargs)

        # apply postprocessing
        processed = effect.postprocess(processed)

        return processed
