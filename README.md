# Visionart Studio
AI-Powered Image Transformation Platform.

## Features
- **Cartoon Effect**: Transform photos into cartoons
- **Oil Painting**: Create Van Goh/Monet style art
- **Pencil Sketch**: Professional sketch effects
- **Image Upscaling**: Enlarge without losing **quality**

## Live Demo
[TBD]

## Tech Stack
- Python
- OpenCV
- Streamlit
- Numpy, PIL

## Project Structure
```text
visionart-studio/
├── main.py                 # Application Entry Point
├── config.py               # Configurations and Constants
├── core/                   # Core Logic
│   ├── __init__.py
│   ├── image_processor.py  # Image processing class 
│   ├── effects/            # effects modules
│   │   ├── __init__.py
│   │   ├── cartoon.py
│   │   ├── oil_painting.py
│   │   ├── pencil_sketch.py
│   │   └── upscaler.py
│   └── utils/              # Utility functions
│       ├── __init__.py
│       ├── file_handlers.py
│       └── image_utils.py
├── ui/                     # User interface components
│   ├── __init__.py
│   ├── components.py
│   ├── layout.py
│   └── sidebar.py
├── services/               # External services (maybe)
│   ├── __init__.py
│   └── analytics.py
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── logo.png
├── requirements.txt
├── setup.py                # Package setup
├── .gitignore
├── pyproject.toml
└── README.md
```


## Vision
This is the first product in the VisionWorks ecosystem - 
a portfolio of computer vision tools ranging from creative
to enterprise solutions.

## Connect
 - Portfolio: [MoOnThePage](https://moonthepage.github.io/)
 - LinkedIn: [Mohammad Ahmad ALhamad — MAAL](https://linkedin.com/in/moonthepage)

