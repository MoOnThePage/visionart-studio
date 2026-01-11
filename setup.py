from setuptools import setup, find_packages

setup(
    name = "visionart-studio",
    version = "1.0.0",
    description = "AI-Powered Image Transformation Platform",
    author = "Mohammad Ahmad ALhammad ",
    author_email = "moonthepage@gmail.com",
    packages = find_packages(),
    install_requires = [
        "numpy>=2.4.0",
        "opencv-contrib-python-headless>=4.11.0.86",
        "pillow>=12.0.0",
        "setuptools>=80.9.0",
        "streamlit>=1.52.2",
    ],
    python_requires = ">=3.11"
)
