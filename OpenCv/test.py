from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from matplotlib import dateutil
img = cv.imread("house.jpg",0)

orb = cv.ORB_create()
kp = orb.detect(img, None)

kp, des = orb.compute(img,kp)
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()

