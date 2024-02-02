import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('box.png', cv.IMREAD_GRAYSCALE)
# Constructor default params: nOctaveLayers = 3,
# contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6
sift = cv.SIFT_create() # construct
kp = sift.detect(img) # detect keypoints
img_with_kp = cv.drawKeypoints(img, kp, img, None,\
cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img_with_kp)
plt.show()