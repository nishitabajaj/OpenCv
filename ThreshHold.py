import numpy as np
import cv2

img = cv2.imread("gradient.png", 0)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('image', img)
cv2.imshow("TH1", th1)
cv2.imshow("TH2", th2)
cv2.imshow("TH3", th3)
cv2.imshow("TH4", th4)
cv2.imshow("TH5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()