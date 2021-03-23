import os, glob, sys
from PIL import Image


basewidth = 300

for infile in glob.glob('.\images\*.png'):
    try:
        file, ext = os.path.splitext(infile)
        img = Image.open(infile)

        if img.size[0] < img.size[1]:



        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        print(img.size)
        img.save(file + '.png', "PNG")
    except IOError:
        print("Cannot create thumbnail for '%s'" % infile)