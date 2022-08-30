'''
pyramid is a multi scale signal representation in which a signal or an image is subject to repeated
smoothing and sub sampling.
Gaussian pyramid :0 repeat filtering & sub sampling of an image.

'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
# lr = cv2.pyrDown(img)
# hr = cv2.pyrUp(img)
layer = img.copy()
gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow("Upper level gaussian pyramid", layer)
lp = [layer]

for i in range(5, 0, -1):
    g_ext = cv2.pyrUp(gp[i])
    lap = cv2.subtract(gp[i-1],g_ext)
    cv2.imshow(str(i), lap)

cv2.imshow('image',img)
# cv2.imshow("Lower resolution", lr)
# cv2.imshow("High resolution", hr)

cv2.waitKey(0)
cv2.destroyAllWindows()