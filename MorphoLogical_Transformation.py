#Morphological transformation are some simple transformations based on the image shape.\
# Normally, performed on binary images.
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE) # also perform for j.png
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.array((2,2), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations = 2)
erosion = cv2.erode(mask, kernel, iterations = 1)

#opening : erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#closing : dilation followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel) # dilation - erosion
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel) # input - opening
blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
ellipse = cv2.morphologyEx(mask, cv2.MORPH_ELLIPSE, kernel)
cross = cv2.morphologyEx(mask, cv2.MORPH_CROSS, kernel)
hitmiss = cv2.morphologyEx(mask, cv2.MORPH_HITMISS, kernel)
rect = cv2.morphologyEx(mask, cv2.MORPH_RECT, kernel)

titles = ['image', 'mask', 'dilation', 'erosion','opening','closing','gradient','tophat',\
          'blackhat','ellipse','cross','hitmiss','rect']
image = [img, mask, dilation, erosion, opening, closing,gradient,tophat,\
         blackhat, ellipse, cross, hitmiss, rect]

for i in range(13):
    plt.subplot(4, 4, i+1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
