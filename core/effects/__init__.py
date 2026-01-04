from . cartoon import CartoonEffect
from . oil_painting import OilPaintingEffect
from . pencil_sketch import PencilSketchEffect
from . upscaler import UpscalerEffect

# Effects fab
def create_effect(effect_name: str):
    """Fabricator function for creating an effect instance"""
    effect = {
        'cartoon': CartoonEffect,
        'oil_painting': OilPaintingEffect,
        'pencil_sketch': PencilSketchEffect,
        'upscaler': UpscalerEffect,
    }

    effect_class = effect.get(effect_name)
    if not effect_class:
        raise ValueError(f"Effect {effect_name} does not exist")

    return effect_class()