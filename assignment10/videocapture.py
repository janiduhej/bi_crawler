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
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        mask = fgbg.apply(frame)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cv2.imshow('Input frame', frame)
        cv2.imshow('Moving objects', mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # q to quit

        cv2.imwrite(img_name, mask)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()
