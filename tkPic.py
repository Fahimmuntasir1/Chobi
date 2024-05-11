# TKPiC - Image processing application.
import cv2
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

# read image from file
img = cv2.imread("nature.jpg")


grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(grayImg, cmap="gray")
plt.show()
