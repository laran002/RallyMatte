import os
import sys
import pathlib
import subprocess

# Usage: generate-iconset.py icon.png
# Automatically generates icons in the icon folder
# based on the favicon image in ./../assets/rallymatte_logo.png

if len(sys.argv) > 1:
    print("Too many arguments")
    raise SystemExit

originalPicture = "./../assets/rallymatte_logo.png"
if not (os.path.isfile(originalPicture)):
    print(f"There is no such file: {originalPicture}")
    raise SystemExit

fname = "app_icon"
ext = ".png"
destDir = "./"

iconsetDir = os.path.join(destDir, f"{fname}.iconset")
if not (os.path.exists(iconsetDir)):
    pathlib.Path(iconsetDir).mkdir(parents=False, exist_ok=True)

class IconParameters():
    width = 0
    scale = 1
    def __init__(self,width,scale):
        self.width = width
        self.scale = scale
    def getIconName(self):
        if self.scale != 1:
            return f"icon_{self.width}x{self.width}{ext}"
        else:
            return f"icon_{self.width//2}x{self.width//2}@2x{ext}"

# https://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/app-icon#app-icon-sizes
ListOfIconParameters = [
    IconParameters(16, 1),
    IconParameters(16, 2),
    IconParameters(32, 1),
    IconParameters(32, 2),
    IconParameters(64, 1),
    IconParameters(64, 2),
    IconParameters(128, 1),
    IconParameters(128, 2),
    IconParameters(256, 1),
    IconParameters(256, 2),
    IconParameters(512, 1),
    IconParameters(512, 2),
    IconParameters(1024, 1),
    IconParameters(1024, 2)
]

# generate iconset
for ip in ListOfIconParameters:
    subprocess.call(
        [
            # option 1: sips
            "sips",
            "-z",
            str(ip.width),
            str(ip.width),
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

# convert iconset to icns file
subprocess.call(
    [
        "iconutil",
        "-c",
        "icns",
        iconsetDir,
        "-o",
        os.path.join(destDir, f"{fname}.icns")
    ]
)
