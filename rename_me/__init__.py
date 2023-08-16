import os
from .config import LOG_DIR

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
    