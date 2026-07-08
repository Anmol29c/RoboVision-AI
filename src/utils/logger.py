"""
Logger Module
RoboVision AI
"""

import logging


def setup_logger(name="RoboVisionAI"):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s - %(message)s",
            datefmt="%H:%M:%S"
        )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger