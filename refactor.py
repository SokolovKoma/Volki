import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageEnhance, Image, ImageFilter
from pytesseract import *


pictures = []
for file in os.listdir(r"C:\Users\Тимофей\PycharmProjects\GoToHackaton\imgs"):
    pictures.append((Image.open(fr"C:\Users\Тимофей\PycharmProjects\GoToHackaton\imgs\{file}"), file,
                     Image.open(fr"C:\Users\Тимофей\PycharmProjects\GoToHackaton\imgs\{file}")))

for picture, path, res in pictures:
    picture = ImageEnhance.Color(picture).enhance(0)
    im_shape = picture.size
    picture = np.array(list(picture.getdata()))
    picture[picture < 200] = 0
    #picture[picture >= 200] = 250
    res.putdata(tuple(map(tuple, picture)))
    #res.show()
    res = ImageEnhance.Sharpness(res.filter(ImageFilter.GaussianBlur(radius=2))).enhance(10)#.filter(ImageFilter.GaussianBlur(radius=2))
    #res.show()
    picture = np.array(list(res.getdata()))
    picture[picture < np.mean(picture[picture != 0]) / 1.5] = 0
    picture = 255 - picture
    res.putdata(tuple(map(tuple, picture)))
    picture = np.array(ImageEnhance.Sharpness(res.filter(ImageFilter.GaussianBlur(radius=2))).enhance(10).getdata())
    picture[picture > 200] = 255
    picture[picture <= 200] = 0
    res.putdata(tuple(map(tuple, picture)))
    #res.show()
    res.save(fr"C:\Users\Тимофей\PycharmProjects\GoToHackaton\preprocessed\{path[:-3] + 'png'}")