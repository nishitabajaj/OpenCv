

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("lena.jpg")
cv2.imshow("image", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

'''
hides ticks values
plt.xticks([])
plt.yticks([])
'''
plt.show()
while True:
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()

#OpenCv reads image BGR format. matplotlib reads image in RGB format.



