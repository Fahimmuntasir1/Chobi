# TKPiC - Image processing application.
import cv2
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

# read image from file
img = cv2.imread("nature.jpg")

# to gray image
# grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# resized = cv2.resize(img, (1080, 720))

rotated90 = cv2.blur(img, (15, 15), 0)
plt.imshow(rotated90, cmap="gray")
plt.show()
