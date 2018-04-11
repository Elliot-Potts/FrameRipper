# 'FrameRipper', Python project to pull still images from a video.
# Written by Elliot Potts: https://github.com/Elliot-Potts
# Have a good day :D

import configparser
import logging
import datetime
import time
import sys
import cv2
import os

settingsDict = {
    'save_prefix': None,
    'max_save': None,
    'default_extension': 'jpg'
}


config = configparser.ConfigParser()
getDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%S-%f")
logging.basicConfig(filename=(getDate+"_frameRipper.log",),
                    level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s - ')


def settingsInit():
    def configCreation():
        os.chdir("C:\Potts' Software\FrameRipper\Settings")
        crConfig = open("main.ini", "w")
        config.add_section("Settings")
        config.set("Settings", "save_prefix", "frameRipper_")
        config.set("Settings", "max_save", "None")
        config.set("Settings", "default_extension", "jpg")

    if os.path.isdir("C:\Potts' Software\FrameRipper\Logging"):
        logging.info("Logging directory found. Continuing.")
    else:
        os.makedirs("C:\Potts' Software\FrameRipper\Logging")
        logging.warning("No logging directory found. Created one and started logger.")

    if os.path.isdir("C:\Potts' Software\FrameRipper\Settings"):
        logging.info("Located settings directory. Will now check for settings file.")
        if os.path.isfile("C:\Potts' Software\FrameRipper\Settings\main.ini"):
            logging.info("Settings file found. Importing.")
        else:
            logging.warning("No settings file found. Creating.")
    else:
        logging.warning("No settings directory found. Creating one, as well as the settings file.")
        os.makedirs("C:\Potts' Software\FrameRipper\Settings")


settingsInit()





