import cv2
import numpy as np
#img = cv2.imread("Lena.jpg",1)
img = np.zeros([512,512,3], dtype = np.uint8)
x = cv2.line(img, (0,0), (255,255), (0,0,255), 5)
y = cv2.arrowedLine(img, (0,255), (255,255), (255,0,255), 5)
r = cv2.rectangle(img, (382,0), (510,128), (0,0,223), -1)
c = cv2.circle(img, (447,63), 63, (0,255,0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
t = cv2.putText(img, "OpenCv",(10,500), font, 4, (255,255,255), 4,cv2.LINE_AA)
print(img)
cv2.imshow("image",img)
k = cv2.waitKey(0)
if k == 27:
     cv2.destroyAllWindows()
elif k == ord("s"):
     cv2.imwrite("lena_copy.png",img)
     cv2.destroyAllWindows()
