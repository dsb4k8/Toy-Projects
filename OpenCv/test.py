from __future__ import division
import matplotlib.pyplot as plt
import cv2
import numpy as np

import matplotlib
from matplotlib import dateutil


orb = cv2.ORB_create()

# cap = cv2.VideoCapture('Drone flight over Skid Row LA - See what happens!.mp4')
cap = cv2.VideoCapture("Drone flight over Skid Row LA - See what happens!.mp4")

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 20
fourcc = cv2.VideoWriter_fourcc(*"H264")

out = cv2.VideoWriter()

success = out.open('output3.avi',fourcc,20.0,(size[0], size[1]))
fr = 0

while True:
    
    ret, frame = cap.read()
    print type(frame)
    if not ret:
        break
    
    kp = orb.detect(frame, None)
    kp, des = orb.compute(frame,kp)
    altered = cv2.drawKeypoints(frame, kp, None, color=(0,255,0), flags=0)
    
    
    gray = cv2.cvtColor(altered,cv2.COLOR_BGR2GRAY)
    
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    rho = 1
    theta = np.pi /180
    threshold = 15
    min_line_length = 50 
    max_line_gap = 20
    line_image = np.copy(altered) * 0
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                    min_line_length, max_line_gap)

    print
    print type(lines)
    print
    if type(lines) is np.ndarray:
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(255,255,0),5)
        lines_edges = cv2.addWeighted(altered, 0.8, line_image, 1, 0)
    else:
        pass


    print type(lines_edges), fr
    out.write(lines_edges)
    fr +=1
    continue
#     plt.imshow(altered), plt.show()
    # if cv2.waitKey(1) & 0xff == ord('q'):
        # break
cap.release()
out.release()
cv2.destroyAllWindows()






