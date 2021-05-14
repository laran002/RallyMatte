import os
import sys
import pathlib
import subprocess

# Usage: generate-iconset.py
# Automatically generates icons in the icon folder
# based on the ./rallymatte_logo.png file

if len(sys.argv) > 1:
    print("Too many arguments")
    raise SystemExit

originalPicture = "./rallymatte_logo.png"
if not (os.path.isfile(originalPicture)):
    print(f"There is no such file: {originalPicture}")
    raise SystemExit

fname = "AppIcon"
ext = ".png"
destDir = "./Assets.xcassets"

iconsetDir = os.path.join(destDir, f"{fname}.appiconset")
if not (os.path.exists(iconsetDir)):
    pathlib.Path(iconsetDir).mkdir(parents=False, exist_ok=True)

class IconParameters():
    width = 0
    scale = 1
    def __init__(self,width,scale):
        self.width = width
        self.scale = scale
    def getIconName(self):
        return f"Icon-App-{self.width}x{self.width}@{self.scale}x{ext}"

# https://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/app-icon#app-icon-sizes
ListOfIconParameters = [
    IconParameters(20, 1),
    IconParameters(20, 2),
    IconParameters(20, 3),
    IconParameters(29, 1),
    IconParameters(29, 2),
    IconParameters(29, 3),
    IconParameters(40, 1),
    IconParameters(40, 2),
    IconParameters(40, 3),
    IconParameters(60, 2),
    IconParameters(60, 3),
    IconParameters(76, 1),
    IconParameters(76, 2),
    IconParameters(83.5, 2),
    IconParameters(1024, 1)
]

# generate iconset
for ip in ListOfIconParameters:
    subprocess.call(
        [
            # option 1: sips
            "sips",
            "-z",
            str(ip.width*ip.scale),
            str(ip.width*ip.scale),
            originalPicture,
            "--out",

            # option 2: ImageMagick
            #"magick",
            #"convert",
            #originalPicture,
            #"-resize",
            #str(ip.width),

            os.path.join(iconsetDir, ip.getIconName())
        ]
    )
    #print(f"Generated {ip.getIconName()}")
