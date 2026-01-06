import streamlit as st
import cv2
import numpy as np
from pathlib import Path
import sys

# modules
from ui.components import header#, before_after_comparison


# Global variables
image = None
processed_image = None
effect = None

def main():
    # Header
    header()

if __name__ == "__main__":
    main()

# File uploading Function
uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "png", "jpeg"])
if uploaded_file:
    # Read the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Display the images
    col1, col2 = st.columns(2)

    # Show the original image
    with col1:
        image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        st.image(image_bgr, caption = "Original Image", width = "content")

    # Effect selection
    effect = st.radio("Choose effect:", ["Cartoon", "Oil Painting", "Pencil Sketch", "Upscale 2X"])

    # Show the edited image
    with col2:
        if effect == "Cartoon":
            # Cartoon effect
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(
                gray,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,9,9
            )
            color = cv2.bilateralFilter(image, 9, 300, 300)
            processed_image = cv2.bitwise_and(color, color, mask = edges)
            processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            st.image(processed_image_rgb, caption = "Cartoon Effect", width = "content")

        elif effect == "Oil Painting":
            # Oil Painting effecting
            processed_image = cv2.xphoto.oilPainting(image, 7, 1)
            processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            st.image(processed_image_rgb, caption = "Oil Painting Effect", width = "content")

        elif effect == "Pencil Sketch":
            # Pencil sketch
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            invert = cv2.bitwise_not(gray)
            blurred = cv2.GaussianBlur(invert, (21, 21), 0)
            inverted_blurred = cv2.bitwise_not(blurred)
            processed_image = cv2.divide(gray, inverted_blurred, scale = 256.0)
            processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            st.image(processed_image_rgb, caption = "Pencil Sketch Effect", width = "content")

        elif effect == "Upscale 2X":
            # Simple upscale (OpenCV)
            height, width = image.shape[:2]
            processed_image = cv2.resize(image, (width * 2, height * 2), interpolation = cv2.INTER_CUBIC)
            processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            st.image(processed_image_rgb, caption = "Upscale 2X Effect", width = "content")

# Download
if processed_image is not None and effect is not None:
    image_to_download = processed_image if processed_image is not None else image

    if len(image_to_download) == 2:
        image_to_download = cv2.cvtColor(image_to_download, cv2.COLOR_GRAY2BGR)

    _, encoded_image = cv2.imencode(".jpg", image_to_download)

    st.download_button(
        label = "Download",
        data = encoded_image.tobytes(),
        file_name = f"visionart_{effect.lower().replace(' ', '_')}.jpg",
        mime = "image/jpeg",
    )