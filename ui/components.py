import streamlit as st
from typing import Dict, Any

def header():
    """Main app header"""
    st.set_page_config(
        page_title="VisionArt Studio",
        page_icon="🔻",
        layout="wide",
    )

    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 2rem, 0;
        }
        
        .effect-card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem 0;
            transition: transform 0.2s;
        }
        
        .effect-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🔻 VisionArt Studio")
        st.markdown("### AI-Powered Image Transformation Platform")
        st.markdown("---")

def effect_selector(effect: Dict[str, Any]) -> str:
    """Effect selection component"""
    st.subheader("🔻 Choose Effect")

    # Create two columns for effect cards
    cols = st.columns(2)

    selected_effect = None
    for idx, (effect_id, effect) in enumerate(effect.items()):
        with cols[idx % 2]:
            with st.container():
                st.markdown(f"<div class='effect-card'>", unsafe_allow_html=True)

                # Effect name and description
                st.markdown(f"***{effect['name']}***")
                st.caption(effect["description"])

                # Premium badge
                if effect.get("premium", False):
                    st.markdown("**Premium**")

                # Select button
                if st.button(f"Select ->", key=f"btn_{effect_id}"):
                    selected_effect = effect_id

                st.markdown(f"</div>", unsafe_allow_html=True)

    return selected_effect

def image_uploader() -> tuple:
    """Image uploader component"""
    st.subheader("upload an Image")

    col1, col2, = st.columns(2)

    with col1:
        upload_method = st.radio(
            "Upload method:",
            ["File Upload", "Camera", "URL"]
        )

    with col2:
        if upload_method == "File Upload":
            uploaded_file = st.file_uploader(
                "Choose an image...",
                type = ["jpg", "jpeg", "png"],
                label_visibility="collapsed"
            )
            return uploaded_file, None
        elif upload_method == "Camera":
            camera_image = st.camera_input("Take a picture")
            return camera_image, None
        else: # URL
            image_url = st.text_input("Image URL")
            return None, image_url

    return None, None

def before_after_comparison(original, processed, effect_name: str):
    """Side-by-side comparison component"""
    st.subheader("Before & After")

    col1, col2 = st.columns(2)

    with col1:
        st.image(original, caption="original image", use_column_width=True)

    with col2:
        st.image(processed, caption=f"{effect_name}", use_column_width=True)
