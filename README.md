## FrameRipper
A Python program to get still images from a video. <br>
I made this with hopes of expanding it in my spare time. I could maybe make a GUI out of it.

## Prerequisites / Requirements
<ol>
<li>Python 3.6+</li>
<li>OpenCV</li>
<li>Webbrowser</li>
<li>datetime</li>
</ol>

## Warnings / Disclaimers / Important notices
<ol>
<li>A 40 second example video I used extracted 1000 frames, at 100MB in size</li>
<li>Extraction can take a while and use a lot of space ^ </li>
<li>If you're skeptical before performing an extraction, simple do: python framerip.py --calculate "path\video"</li>
<li>Extracting frames with the BMP file extension dramatically reduces extraction time, but can product unpredictable outcomes</li>
</ol>

## Command-line arguments / usage
In the examples below, I'm assuming python 3 (alternative) has been added to your path, and that you have kept the
script name the same: framerip.py
 1. python framerip.py --video "path/video.extension" <br>
Starts the extraction process on the specified video. Quotes must be included.
 2. python framerip.py --help <br>
Displays information about the program.
 3. python framerip.py --calculate "path/video.extension" <br>
Shows information about the extraction before you do it. Useful if you want to know file size.
 4. python framerip.py --gui <br>
When implemented: would start the graphical interface for the program
 5. python framerip.py --save-prefix < save prefix><br>
Changes the configuration file with a new prefix, used when extracting frames.
 6. python framerip.py --max-frames < max frame number ><br>
Must be an integer, or None; this changes the configuration file with a maximum amount of frames. Useful if you don't want to filebomb your own computer :)
 7. python framerip.py --extension < extension ><br>
Changes the extension (JPG, PNG, BMP, etc) for the extracted frames.
 8. python framerip.py --directory < directory ><br>
Changes the export directory for the frames

Have a good day!
