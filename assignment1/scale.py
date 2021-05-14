import numpy as np
import cv2
import os

# setup
path = 'avatar.jpg'
path_scaled = 'avatar_size.jpg'
interpolation_type = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_AREA, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]
interpolation_idx = 0
scale_factor = 100
scale_min = 10
scale_max = 200
print(interpolation_type)
if os.path.exists(path_scaled):
    os.remove(path_scaled)

# create window and load image
title = 'Sloth'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.resizeWindow(title, 704, 528)
img = cv2.imread(path, 1)


def on_set_interpolation_type(value):
    interpolation_idx = value


def on_set_scale(value):
    scale = value / scale_factor
    newimg = cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)),
                        interpolation=interpolation_type[interpolation_idx])
    cv2.resizeWindow(title, newimg.shape[1], newimg.shape[0])
    cv2.imshow(title, newimg)
    cv2.imwrite(path_scaled, newimg)


# add sliders
cv2.createTrackbar('Interpolation Type', title, 0, len(interpolation_type) - 1, on_set_interpolation_type)
cv2.createTrackbar('Scale', title, scale_min, scale_max, on_set_scale)

while (True):
    # load the rescaled image
    if os.path.isfile(path_scaled):
        img = cv2.imread(path_scaled, 1)

    cv2.imshow(title, img)

    if cv2.waitKey(0) != 0:
        break

# cleanup
cv2.destroyAllWindows()


