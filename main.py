# 'FrameRipper', Python project to pull still images from a video.
# Written by Elliot Potts: https://github.com/Elliot-Potts :D

import configparser
import logging
import datetime
import time
import sys
import cv2
import os

getDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%S-%f")
logging.basicConfig(filename=(getDate+"_frameRipper.log",),
                    level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s - ')


def settingsInit():
    if os.path.isfile("C:\Potts' Software\FrameRipper\Logging"):
        logging.info("Logging directory found. Continuing.")
    else:
        os.makedirs("C:\Potts' Software\FrameRipper\Logging")
        logging.warning("No logging directory found. Created one and started logger.")

    if os.path.isfile("C:\Potts' Software\FrameRipper\Settings"):
        logging.info("Located settings directory.")
    else:
        logging.warning("No settings directory found. Creating one.")
        os.makedirs("C:\Potts' Software\FrameRipper\Settings")


settingsInit()

