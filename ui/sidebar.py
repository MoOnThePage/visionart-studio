import streamlit as st
from typing import Dict, Any

def app_sidebar(effects: Dict[str, Any]):
    """Application sidebar with settings"""
    with st.sidebar:
        st.markdown("## Settings")

        # Effect configuration
        selected_effect = st.selectbox(
            "Select effect",
            options=list(effects.keys()),
            format_func=lambda x: effects[x]["name"]
        )

        # Effect-specific settings
        st.markdown("## Effect Settings")

        if selected_effect == "cartoon":
            blur_size = st.slider("Blur Size", 3, 15, 5, 2)
            edge_threshold = st.slider("Edge Threshold", 3, 15, 9, 2)
            return {
                "effect": selected_effect,
                "blur_size": blur_size,
                "edge_threshold": edge_threshold
            }
        elif selected_effect == "oil_painting":
            brush_size = st.slider("Brush Size", 1, 15, 7, 2)
            intensity = st.slider("Intensity", 1, 10, 1)
            return {
                "effect": selected_effect,
                "size": brush_size,
                "dynRation": intensity
            }
        elif selected_effect == "pencil_sketch":
            blur_amount = st.slider("Blur Amount", 5, 51, 21, 2)
            return {
                "effect": selected_effect,
                "blur_kernel": (blur_amount, blur_amount),
            }
        elif selected_effect == "upscale":
            scale_factor = st.slider("Scale Factor", [2, 3, 4], index = 0)
            return {
                "effect": selected_effect,
                "scale_factor": scale_factor
            }
        return {"effect": selected_effect}
