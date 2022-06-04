from PIL import Image, ImageDraw

img_mask = Image.new('RGBA',(420,230),(0,0,0,255))
draw = ImageDraw.Draw(img_mask)
draw.rectangle((30,30,130,130),fill=(255,255,255,0))
draw.rectangle((140,30,240,130),fill=(255,255,255,0))
draw.rectangle((250,30,350,130),fill=(255,255,255,0))
img_mask.save('./images/mask.png')
