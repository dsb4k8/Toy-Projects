from __future__ import division
import matplotlib.pyplot as plt
import cv2
import numpy as np

import matplotlib
from matplotlib import dateutil






# img = cv.imread("house.jpg",0)

# orb = cv.ORB_create()
# kp = orb.detect(img, None)

# kp, des = orb.compute(img,kp)
# img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
# plt.imshow(img2), plt.show()
orb = cv2.ORB_create()

cap = cv2.VideoCapture('Relaxing Ride to Acapulco Mexico  G310R  390 Duke.mp4')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 20
fourcc = cv2.VideoWriter_fourcc(*"H264")

out = cv2.VideoWriter()

success = out.open('output.avi',fourcc,20.0,(size[0], size[1]))
fr = 0
while True:
    
    ret, frame = cap.read()
    print type(frame)
    if not ret:
        break

    kp = orb.detect(frame, None)
    kp, des = orb.compute(frame,kp)
    altered = cv2.drawKeypoints(frame, kp, None, color=(0,255,0), flags=0)
    print type(altered), fr
    out.write(altered)
    fr +=1
    continue
#     plt.imshow(altered), plt.show()
    # if cv2.waitKey(1) & 0xff == ord('q'):
        # break
cap.release()
out.release()
cv2.destroyAllWindows()






