import os, glob, sys
from PIL import Image


size = 300, 300

for infile in glob.glob('.\images\*.png'):
    try:
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + '.png', "PNG")
    except IOError:
        print("Cannot create thumbnail for '%s'" % infile)