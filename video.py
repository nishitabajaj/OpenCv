import cv2
import datetime
x = cv2.VideoCapture(0);
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("output.avi",fourcc,20.0,(4,3))
print(x.get(cv2.CAP_PROP_FRAME_WIDTH))
print(x.get(cv2.CAP_PROP_FRAME_HEIGHT))
# x.set(3, 1245)
# x.set(4, 600)
#
# print(x.get(3))
# print(x.get(4))
while(x.isOpened()):
    ret, frame = x.read()
    if(ret== True):
        # print(cv2.get(CAP_PROP_FRAME_WIDTH))
        # print(cv2.get(CAP_PROP_FRAME_HEIGHT))
        #out.write(frame)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width :" + str(x.get(3)) + "HEIGHT: " + str(x.get(4))
        datet = str(datetime.datetime.now())

       #frame = cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
x.release()
#out.release()
cv2.destroyAllWindows()