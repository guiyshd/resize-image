import os, glob, sys
from PIL import Image


def resize(width, height):
    """Return resized image"""
    for infile in glob.glob('images/*.jpg'):
        try:
            im = Image.open(infile)
            im.thumbnail([width, height], Image.ANTIALIAS)
            im.save('images/' + ".jpg", "JPG")
        except IOError:
            print("Cannot create thumbnail for '%s'" % infile)
    return


resize(300, 300)