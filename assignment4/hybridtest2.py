# Python program for blending of
# images using OpenCV

# import OpenCV file
import cv2

# Read Image1
john = cv2.imread('John_blending2.png', 0)

# Read image2
marylin = cv2.imread('Marylin_blending2.png', 0)

# Blending the images with 0.3 and 0.7
img = cv2.addWeighted(john, 0.3, marylin, 0.7, 0)

# Show the image
cv2.imshow('image', img)

# Wait for a key
cv2.waitKey(0)

# Destroy all the window open
cv2.distroyAllWindows()