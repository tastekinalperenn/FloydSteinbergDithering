import matplotlib.pyplot as plt
import matplotlib.image as matplotpimg
from PIL import Image 
import numpy as np


def FloydSteinberg(image,q):
    for y in range(len(image)-1):
        for x in range(len(image[0])-1):
           oldpixel = image[y][x]
           newpixel=np.round(oldpixel/q)*q
           quant_error = oldpixel - newpixel
           image[y+1][x] = image[y+1][x] + quant_error * 7 /16
           image[y-1][x+1] = image[y-1][x+1] + quant_error * 3 /16
           image[y][x+1] = image[y][x+1] + quant_error * 5 /16
           image[y+1][x+1] = image[y+1][x+1] + quant_error * 1 /16
    

    plt.imshow(image)  # image shown as matplotlib plot
          

imageWithReadingPIL = Image.open("1.png") 
imageWithReadingPIL=imageWithReadingPIL.quantize(32)
imageWithReadingPIL.show()  

  
#We read image again because dithering with matplotlib
imageWihtReadingPlot = matplotpimg.imread("1.png") 
FloydSteinberg(imageWihtReadingPlot,32)