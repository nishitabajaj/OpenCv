import numpy as np
import matplotlib.pyplot as plt
import cv2

x = cv2.imread("gradient.png")
ret, th1 = cv2.threshold(x,50,255,cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(x,200,255,cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(x,127,255,cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(x,127,255,cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(x,127,255,cv2.THRESH_TOZERO_INV)

titles = ['ORIGINAL', 'BINARY', 'BINARY INV', 'TRUNC', 'TOZERO', 'TOZERO INV']
images = [x, th1, th2, th3, th4, th5 ]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()