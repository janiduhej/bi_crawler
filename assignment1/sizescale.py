import numpy as np
import cv2
from matplotlib import pyplot as plt


# Load an color image in grayscale
img = cv2.imread('avatar.jpg',cv2.IMREAD_UNCHANGED)


print('Original Dimensions : ', img.shape)

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)



# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imshow("Resized image", resized)
cv2.imwrite('avatar_size.png',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()