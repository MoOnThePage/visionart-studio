import streamlit as st
import cv2
import numpy as np
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# modules
from config import EFFECTS, SUPPORTED_EXTENSIONS
from core.image_processor import ImageProcessor
from core.effects import create_effect
from core.utils.image_utils import bytes_to_image, image_to_bytes, resize_image

from ui.sidebar import app_sidebar
from ui.components import header, before_after_comparison

from services.analytics import Analytics

def initialize_processor() -> ImageProcessor:
    """Initialize the image processor with all effects"""
    processor = ImageProcessor()

    # Register all effects
    for effect_name in EFFECTS.keys():
        effect = create_effect(effect_name)
        processor.register_effect(effect_name, effect)

    return processor

def main():
    """Main application function"""

    # Initialize
    processor = initialize_processor()
    analytics = Analytics()

    # Page Header
    header()

    # Sidebar for settings
    settings = app_sidebar(EFFECTS)
    selected_effect = settings["effect"]

    # Track usage
    analytics.log_usage(
        "effect_selected", {
            "effect": selected_effect,
            "settings": settings
        }
    )
    analytics.increment_stat(f"effect_{selected_effect}_selected")

    # File upload section
    st.subheader("Upload image")

    col1, col2 = st.columns([2, 1])

    with col1:
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type = SUPPORTED_EXTENSIONS,
            label_visibility="collapsed"
        )

    with col2:
        if uploaded_file:
            file_size = len(uploaded_file.getvalue()) / 1024 / 1024 #MB
            st.info(f"File size: {file_size:.2f} MB")

    # Main processing section
    if uploaded_file:
        try:
            # convert to image
            file_bytes = uploaded_file.getvalue()
            original_image = bytes_to_image(file_bytes)

            # Resize if too large
            original_image = resize_image(original_image)

            # Create columns for comparison
            col1, col2 = st.columns(2)

            with col1:
                st.image(original_image, caption="Original Image", use_column_width=True)

            # process button
            if st.button("🪄 Apply Effect", type="primary", use_container_width=True):
                with st.spinner(f"Magic Spell{EFFECTS[selected_effect]['name']}..."):
                    # Apply effect
                    processed_image = processor.process(
                        selected_effect,
                        original_image,
                        **{k: v for k, v in settings.items() if k != "effect"}
                    )

                    # Show result
                    with col2:
                        st.image(
                            processed_image,
                            caption=f"{EFFECTS[selected_effect]['name']}",
                            use_column_width=True
                        )

                    # Download button
                    processed_bytes = image_to_bytes(processed_image)

                    st.download_button(
                        label="🔻 Download Result",
                        data=processed_bytes,
                        file_name=f"visionart_{selected_effect}.png",
                        mime="image/jpeg",
                        use_container_width=True
                    )

                    # Track successful processing
                    analytics.increment_stat("images_processed")
                    st.success("Effect successfully applied!")
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            st.info("Please try a different image or adjust the settings")

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center;">
        <p>🔻 <b>VisionArt Studio</b> - Part of VisionWorks Ecosystem</p>
        <p>Built with 🎔 using OpenCV & Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()