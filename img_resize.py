from PIL import Image

img  =  Image.open('./images/button_yellow.png')
img_resize = img.resize((100,40))
img_resize.save('./images/button_yellow.png')