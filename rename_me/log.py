import logging

from .config import LOG_DIR, DEBUG
    
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logging.basicConfig(
        level=logging.DEBUG if DEBUG else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(f"{LOG_DIR}{name}.log"),
            logging.StreamHandler()
        ]
    )
    return logger

