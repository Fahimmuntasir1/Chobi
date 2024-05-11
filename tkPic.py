# TKPiC - Image processing application.
import cv2

# read image from file
img = cv2.imread("img/nature.jpg")

imGray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
# to show image
cv2.imshow("output", img)

cv2.waitKey(0)
