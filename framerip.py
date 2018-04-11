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

getDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%S-%f")
config = configparser.ConfigParser()
settingsDict = {
    'save_prefix': None,
    'max_save': None,
    'extension': 'jpg',
    'save_directory': "C:\Potts' Software\Frame Ripper\Extracted Frames"
}


def loggingInit():
    os.chdir("C:\Potts' Software\Frame Ripper\Logging")
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
        config.set("Settings", "extension", "jpg")
        config.set("Settings", "directory", "C:\Potts' Software\Frame Ripper\Extracted Frames")
        config.write(crConfig)
        crConfig.close()

    def configImport():
        os.chdir("C:\Potts' Software\Frame Ripper\Settings")
        openConfig = config.read("main.ini")
        settingsDict['save_prefix'] = config.get("Settings", "save_prefix")
        settingsDict['max_save'] = config.get("Settings", "max_save")
        settingsDict['extension'] = config.get("Settings", "extension")
        settingsDict['save_directory'] = config.get("Settings", "directory")

    if os.path.isdir("C:\Potts' Software\Frame Ripper\Extracted Frames"):
        pass
    else:
        os.makedirs("C:\Potts' Software\Frame Ripper\Extracted Frames")

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


def extractFrames(video_name, full_path):
    # pathToVideo = os.path.dirname(os.path.relpath(full_path))

    vidCap = cv2.VideoCapture(full_path)

    frameAmount = int(vidCap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameAmount2 = int(vidCap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("-- Press enter to continue --")
    print1 = input("About to begin extracting {} frames from {}".format(str(frameAmount), video_name))
    print2 = input("This may take a while. Feel free to cancel at any moment with Ctrl+C.")
    print("-- Extracting in 5 seconds --")

    time.sleep(5)

    success, image = vidCap.read()

    opStartTime = time.time()

    os.chdir(settingsDict['save_directory'])
    saveDir = "{}_{}_renderedFrames".format(video_name, str(getDate))
    os.mkdir(saveDir)
    os.chdir(saveDir)

    counter = 0
    success = True

    while success:
        success, image = vidCap.read()
        cv2.imwrite(("{}{}_frame_{}.{}".format(settingsDict['save_prefix'], video_name, str(counter), settingsDict['extension'])),
                                              image)
        print("Successfully extracted frame {}. {}/{} frames left.".format(
            str(counter), str(frameAmount2 - counter), str(frameAmount)
        ))
        counter += 1

    opEndTime = time.time()
    opFinalTime = opEndTime - opStartTime
    print("Operation completed. Extracted {} frames in {} seconds.".format(
        str(frameAmount), str(opFinalTime)
    ))


def checkArgs():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "--info":
            print(r"""------------------------
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
--website : displays my websites :) 

--video "<video.extension>" : will start grabbing frames from this video, 
                              make sure to include quotation marks

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
            settingsDict['extension'] = sys.argv[2]
        elif sys.argv[1] == "--directory":
            print("Changing the export directory to: {}".format(str(sys.argv[2])))
            settingsDict['save_directory'] = sys.argv[2]
        elif sys.argv[1] == "--video":
            # print("File path entered: {}".format(sys.argv[2]))
            # print(os.path.dirname(os.path.realpath(sys.argv[2])))
            videoName = os.path.basename(sys.argv[2])
            print("Are you sure you want to extract frames from video {} to directory {}?".format(videoName,
                                                                                str(settingsDict['save_directory'])))

            getExpConf = input("Enter Y/N: ").lower()

            if getExpConf == "y":
                extractFrames(videoName, sys.argv[2])
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

logging.info("Saving the settings from the session.")

os.chdir("C:\Potts' Software\Frame Ripper\Settings")
crConfig = open("main.ini", "w")
try:
    config.add_section("Settings")
except configparser.DuplicateSectionError:
    pass
config.set("Settings", "save_prefix", str(settingsDict['save_prefix']))
config.set("Settings", "max_save", str(settingsDict['max_save']))
config.set("Settings", "extension", str(settingsDict['extension']))
config.set("Settings", "directory", str(settingsDict['save_directory']))
config.write(crConfig)
crConfig.close()

logging.info("Settings have been saved at the end of the session.")




