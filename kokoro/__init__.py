__version__ = '0.9.4'

from loguru import logger
import sys
import os

# Remove default handler
logger.remove()

# Add custom handler with clean format including module and line number
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <cyan>{module:>16}:{line}</cyan> | <level>{level: >8}</level> | <level>{message}</level>",
    colorize=True,
    level="INFO"  # "DEBUG" to enable logger.debug("message") and up prints
                   # "ERROR" to enable only logger.error("message") prints
                   # etc
)

# Disable before release or as needed
logger.disable("kokoro")

# Ensure espeak-ng uses the packaged library and data path before any imports
# that initialize phonemizer/espeak. This avoids failures looking for phontab
# in non-existent CI build paths on some platforms.
try:
    import espeakng_loader  # provided by dependency

    # Point phonemizer to the correct espeak-ng shared library explicitly.
    # Phonemizer honors this variable when selecting the library.
    os.environ.setdefault("PHONEMIZER_ESPEAK_LIBRARY", espeakng_loader.get_library_path())

    # espeak-ng honors these variables for locating its data directory.
    data_path = espeakng_loader.get_data_path()
    os.environ.setdefault("ESPEAKNG_DATA_PATH", data_path)
    # Older variable name used by espeak (legacy), set as well for safety.
    os.environ.setdefault("ESPEAK_DATA_PATH", data_path)
except Exception:
    # If espeakng_loader is unavailable, continue; environments with system
    # espeak-ng installed may still work. We avoid hard failure here.
    pass

from .model import KModel
from .pipeline import KPipeline
