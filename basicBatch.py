
from PIL import Image
from PIL import ImageFilter
from os import listdir

def cropIm(im):
    print(im.format, im.size, im.mode)
    # im.show()

    filters = [ImageFilter.SHARPEN, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.FIND_EDGES]
    imf = im

    for f in filters:
        imf = imf.filter(f)

    # imf.show()

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

    y = findEdge(imf.height, 100, True)
    x = findEdge(imf.width, y, False)

    imc = im.crop((0,0,x,y))
    imc.show()

paths = listdir("testImages")

for pth in paths:
    im = Image.open("testImages/" + pth)
    cropIm(im)