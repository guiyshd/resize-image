import os, glob, sys
from PIL import Image


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

basewidth = 300

for infile in glob.glob('.\images\*.jpg'):
    try:
        file, ext = os.path.splitext(infile)
        img = Image.open(infile)

        print(file, "Antes", img.size)

        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        
        print(file, "Depois", img.size) 

        img.save(file + '.png', "PNG")
    except IOError:
        print("Cannot create thumbnail for '%s'" % infile)