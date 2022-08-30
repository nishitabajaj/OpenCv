#image gradient is a directional change in intensity or color of an image.

import numpy as np
import matplotlib.pyplot as plt
import cv2
img = cv2.imread('messi5.jpg',0)
#img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE) # for sobel
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) #detects the edges of an image
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0) #img , dtype, dx=order of derivative x, dy = order of derivative y, ksize=op.
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelx=np.uint8(np.absolute(sobelx)) # change in vertical direction or x axis
sobely=np.uint8(np.absolute(sobely)) # change in horizontal direction or y axis
sobelCombined = cv2.bitwise_or(sobelx, sobely)

scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharrx = np.uint8(np.absolute(scharrx))
scharry = np.uint8(np.absolute(scharry))
scharrCombined = cv2.bitwise_or(scharrx, scharry)
edges = cv2.Canny(img, 100, 200)

titles = ['image','Laplacian','sobelx','sobely','sobelCombined','ScharrX','ScharrY','scharrCombined','edges']
images = [img, lap, sobelx, sobely, sobelCombined,scharrx, scharry, scharrCombined,edges]

for i in range(9):
    plt.subplot(3, 3, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()