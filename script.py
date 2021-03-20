from PIL import Image

baseCalculo = (300/2)

img = Image.open('images/fullsized_image.png')
width, height = img.size
print(img.size)
le = (width/2)-baseCalculo
up = (height/2)-baseCalculo
ri = (width/2)-baseCalculo
lo = (height/2)-baseCalculo

# area = (le, up, ri, lo)
# print(area)
# img_crop = img.crop(area)
# print(img_crop.size)

(left, upper, right, lower) = (le, up, width-ri, height-lo)

# Here the image "im" is cropped and assigned to new variable im_crop
im_crop = img.crop((left, upper, right, lower))
print(im_crop.size)

im_crop.save('images/resized_image.png')
# img_crop.save('images/resized_image.png')