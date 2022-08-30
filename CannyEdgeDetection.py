
'''
Canny edge detector is an edge detection operator that uses a multi stage algorithm to detect a wide range of
edges in images . It was developed by John F. Canny in 1986.
Steps:
Noise Reduction
Gradient Calculation
Non - maximum suppression
Double Threshold
Edge tracking by hysteresis
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', 0)

canny = cv2.Canny(img, 100, 200)

title = ['image','canny']
images = [img, canny]

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.title(title[i])

plt.show()