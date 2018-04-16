# Testing done for the statistics calculator
# Testing here will be to test file size calculation, framerate calculation etc.
# Written by Elliot Potts: https://github.com/Elliot-Potts
# Have a good day :D


from hurry.filesize import size
import cv2
import os


if os.path.isdir("C:\Potts' Software\Frame Ripper\Temp"):
    pass
else:
    os.mkdir("C:\Potts' Software\Frame Ripper\Temp")

os.chdir("C:\Potts' Software\Frame Ripper\Temp")

vid = cv2.VideoCapture(r"C:\Users\Poots\Desktop\Development\Python\SkyZun Software\FrameRipper\FrameRipper\example_video.mp4")

success, image = vid.read()

cv2.imwrite("testFrame.jpg", image)

estimFileSize = os.path.getsize(r"C:\Potts' Software\Frame Ripper\Temp\testFrame.jpg")

multiEstimFileSize = estimFileSize * int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

formattedFileSize = size(multiEstimFileSize)

print("Size in bytes: {} \n Size formatted: {}".format(str(estimFileSize), str(formattedFileSize)))

