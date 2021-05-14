import cv2
import numpy as np


# read left and right images
# images from https://medium.com/pylessons/image-stitching-with-opencv-and-python-1ebd9e0a6d78
left = cv2.imread('./images/zebra.png')
right = cv2.imread('./images/horse.png')

# increase brightness of right image so that the blend difference can be seen after stitching
rightx = 1.5*right
rightx = np.clip((rightx), 0, 255)
rightx = np.uint8(rightx)

# get dimensions
hl, wl, cl = left.shape
hr, wr, cr = right.shape

print("left",hl,wl)
print("right",hr,wr)
#left 768 1024
#right 768 1024

crop1 = left[0:hl, 0:int(wl/2)]
crop2 = right[0:hr, int(wr/2):wr]




# concatenate the images for the stitched result
stitched = np.concatenate((crop1,crop2), axis=1)
cv2.imwrite('directblend.png',stitched)
cv2.imshow("stitched", stitched)
cv2.waitKey(0)
cv2.destroyAllWindows()
