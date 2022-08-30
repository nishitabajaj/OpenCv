import numpy as np
import cv2
import matplotlib.pyplot as plt

#homogenous filter : Most simple filter, Each output pixel is the mean of its kernel nieighbours
#kernel is a shape which we can apply over an image.
#blur is used to make the image blur.
#Gaussian filter is used for removing high noise from the image.
#median filter replaces each pixel's value with the median of its neighbouring pixels.Removes salt and pepper noise.
#bilateralfilter preserves the borders. Removes the noise while keeping the edges sharp.

img = cv2.imread('lena.jpg') #bilateral filter
#img = cv2.imread('flower.png') #used with median filter
#img = cv2.imread('Halftone_Gaussian_Blur.jpg') #used with gaussian blur
#img = cv2.imread('opencv-logo-white.png') #used with blur, filter2D
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img , 3)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) #sigmacolor,sigmaspace

titles = ['image','2D-Convolution','blur','gaussian blur','medianfilter','bilateralFilter']
images = [img,dst, blur, gaussian, median,bilateralFilter]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()