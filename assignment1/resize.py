import cv2
import numpy as np

cv2.namedWindow('window')
fill_val = np.array([255, 255, 255], np.uint8)
def trackbar_callback(idx, value):
    fill_val[idx] = value


img = cv2.imread('avatar.jpg')


img_scaled = cv2.resize(img,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Scaling - Linear Interpolation', img_scaled)
img_scaled = cv2.resize(img,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)
img_scaled = cv2.resize(img,(450, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled)

cv2.waitKey()
print('original image shape:', img.shape)

cv2.imwrite('scaled.jpg', img_scaled)
orig = cv2.imread('avatar.jpg')
orig_size = orig.shape[0:2]
cv2.imshow("Original image", orig)
cv2.waitKey(2000)