from camera.camera import Camera
from utils.logger import setup_logger

logger = setup_logger()


def main():
    logger.info("Starting RoboVision AI...")

    camera = Camera()
    camera.run()

    logger.info("Application Closed")


if __name__ == "__main__":
    main()