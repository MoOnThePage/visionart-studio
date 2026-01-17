import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
# STATIC_DIR = BASE_DIR / "static"
# UPLOAD_DIR = STATIC_DIR / "uploads"
# UPLOAD_DIR.mkdir(exist_ok = True)

# App Config
APP_NAME = "VisionArt Studio"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "Artistic Image Processing"

# Supported files
SUPPORTED_EXTENSIONS = [".jpeg", ".jpg", ".jpe", ".png", ".tiff", ".tif", ".bmp", ".dib", ".webp", ".jp2",
                        ".gif", ".sr", ".ras", ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".hdr", ".pic"]

# Effect Configuration
EFFECTS = {
    "cartoon": {
        "name": "Cartoon Effect",
        "description": "Transform photos into cartoons",
        "category": "artistic",
        "premium": False,
    },
    "oil_painting": {
        "name": "Oil Painting Effect",
        "description": "Van Goh/Monet Style Oil painting",
        "category": "artistic",
        "premium": False,
    },
    "pencil_sketch": {
        "name": "Pencil Sketch Effect",
        "description": "Professional pencil sketch",
        "category": "artistic",
        "premium": False,
    },
    "upscale": {
        "name": "Upscale 2X",
        "description": "Enlarge image without quality loss",
        "category": "enhancement",
        "premium": False,
    }
}

# Processing parameters
DEFAULT_IMAGE_SIZE = (800, 800)
MAX_FILE_SIZE_MB = 10