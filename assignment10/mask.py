


import cv2
import multiprocessing as mp
num_workers = mp.cpu_count()
print(num_workers)
import tensorflow
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

cam = cv2.VideoCapture(0)

fgbg= cv2.createBackgroundSubtractorKNN()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(3,3))
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if frame is None:
        break

    fgMask = fgbg.apply(frame)

    cv2.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv2.putText(frame, str(cam.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cam.release()