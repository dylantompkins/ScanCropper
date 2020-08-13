
from PIL import Image
im = Image.open("testImg.jpg")
print(im.format, im.size, im.mode)
im.show()

from PIL import ImageFilter
filters = [ImageFilter.EMBOSS, ImageFilter.SMOOTH_MORE, ImageFilter.FIND_EDGES, ImageFilter.EDGE_ENHANCE]
imf = im

for f in filters:
    imf = imf.filter(f)

imf.show()

px = imf.load()

def getPx(i, offset, vert):
    if (vert):
        return px[offset, i]
    else:
        return px[i, offset]

def findEdge(upperBounds, offset, vert):
    for i in range(upperBounds - 1, 0, -1):
        if (getPx(i, offset, vert) == (255, 255, 255)):
            return i

x = findEdge(imf.width, 100, False)
y = findEdge(imf.height, 100, True)

imc = im.crop((0,0,x,y))
imc.show()