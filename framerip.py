# 'FrameRipper', Python project to pull still images from a video.
# Written by Elliot Potts: https://github.com/Elliot-Potts
# Have a good day :D

import configparser
import webbrowser
import logging
import datetime
import time
import sys
import cv2
import os

config = configparser.ConfigParser()
settingsDict = {
    'save_prefix': None,
    'max_save': None,
    'default_extension': 'jpg',
    'save_directory': None
}


def loggingInit():
    os.chdir("C:\Potts' Software\Frame Ripper\Logging")
    getDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%S-%f")
    logging.basicConfig(filename=getDate+"_frameRipper"+".log",
                        level=logging.DEBUG,
                        format='%(levelname)s - %(asctime)s - %(message)s')


def settingsInit():
    def configCreation():
        os.chdir("C:\Potts' Software\Frame Ripper\Settings")
        crConfig = open("main.ini", "w")
        config.add_section("Settings")
        config.set("Settings", "save_prefix", "frameRipper_")
        config.set("Settings", "max_save", "None")
        config.set("Settings", "default_extension", "jpg")
        config.write(crConfig)
        crConfig.close()

    def configImport():
        os.chdir("C:\Potts' Software\Frame Ripper\Settings")
        openConfig = config.read("main.ini")
        settingsDict['save_prefix'] = config.get("Settings", "save_prefix")
        settingsDict['max_save'] = config.get("Settings", "max_save")
        settingsDict['default_extension'] = config.get("Settings", "default_extension")

    if os.path.isdir("C:\Potts' Software\Frame Ripper\Logging"):
        loggingInit()
        logging.info("Logging directory found. Continuing.")
    else:
        os.makedirs("C:\Potts' Software\Frame Ripper\Logging")
        loggingInit()
        logging.warning("No logging directory found. Created one and started logger.")

    if os.path.isdir("C:\Potts' Software\Frame Ripper\Settings"):
        logging.info("Located settings directory. Will now check for settings file.")
        if os.path.isfile("C:\Potts' Software\Frame Ripper\Settings\main.ini"):
            logging.info("Settings file found. Importing.")
            configImport()
            logging.info("Configuration import function passed successfully.")
        else:
            logging.warning("No settings file found. Creating.")
            configCreation()
            logging.info("Configuration creation function passed successfully.")
    else:
        logging.warning("No settings directory found. Creating one, as well as the settings file.")
        os.makedirs("C:\Potts' Software\Frame Ripper\Settings")


settingsInit()
logging.info("Settings function has been passed without problem.")


def checkArgs():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "--info":
            print("""------------------------
Frame Ripper Help & Info
------------------------
Written by Elliot Potts
https://elliotpotts.me/
https://github.com/Elliot-Potts/
------------------------
CLI Arguments & Usage:
------------------------
--help : displays help and info message
--info : displays help and info message
--website : displays my websites

--video <video.extension> : will start grabbing frames from this video

--gui : starts GUI application
            *may not be completed*

--save-prefix <save prefix> : sets the new save prefix for saved frames
--max-frames <max frame number> : sets the new amount of max frames
                                    (must be integer or 'None')
--extension <extension> : sets the extension
--directory <directory> : sets the directory
                            this will set the value in the config file, change this when you want to save elsewhere
------------------------
    """)
            logging.info("Help argument detected. Ran and finished.")
        elif sys.argv[1] == "--website":
            webbrowser.open("https://elliotpotts.me")
            webbrowser.open("https://github.com/Elliot-Potts")
            logging.info("Website argument detected. Ran and finished.")
        elif sys.argv[1] == "--gui":
            print("GUI has not been implemented yet.")
        elif sys.argv[1] == "--save-prefix":
            print("Changing save prefix to: {}".format(str(sys.argv[2])))
            settingsDict['save_prefix'] = sys.argv[2]
        elif sys.argv[1] == "--max-frames":
            print("Changing max frames/limit to: {}".format(str(sys.argv[2])))
            settingsDict['max_save'] = sys.argv[2]
        elif sys.argv[1] == "--extension":
            print("Changing extension to: {}".format(str(sys.argv[2])))
            settingsDict['default_extension'] = sys.argv[2]
        elif sys.argv[1] == "--directory":
            print("Changing the export directory to: {}".format(str(sys.argv[2])))
            settingsDict['save_directory'] = sys.argv[2]
        elif sys.argv[1] == "--video":
            print("Are you sure you want to extract frames from video {} to directory {}?".format(str(sys.argv[2]),
                                                                                str(settingsDict['save_directory'])))
            getExpConf = input("Enter Y/N: ").lower()
            if getExpConf == "y":
                print("Continuing. Please allow time dependent on how big your video is. This may take a while.")
            elif getExpConf == "n":
                print("You aborted. Exiting.")
                sys.exit()
            else:
                print("Invalid input. Enter Y/N.")
                sys.exit()
        else:
            print("Invalid program usage.")
            print("Type python framerip.py --help for more information.")
    except IndexError:
        print("Invalid program usage.")
        print("Type python framerip.py --help for more information.")


checkArgs()







