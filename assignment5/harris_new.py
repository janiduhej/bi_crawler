import cv2


def funcRotate(degree=0):
    degree = cv2.getTrackbarPos('degree', 'Rotate')
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    rotated_image = cv2.warpAffine(original, rotation_matrix, (width, height))
    cv2.imshow('Rotate', rotated_image)


if __name__ == '__main__':
    original = cv2.imread("./images/testbild.jpg", 1)
    height, width = original.shape[:2]
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)


    cv2.namedWindow('Rotate')
    degree = 0
    cv2.createTrackbar('degree', 'Rotate', degree, 360, funcRotate)
    funcRotate(0)
    dst = cv2.cornerHarris(gray, 9, 13, 0.04)
    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    threshold = 0.005
    original[dst > threshold * dst.max()] = [0, 0, 255]

    cv2.imshow('Rotate', original)
    cv2.waitKey(0)

cv2.destroyAllWindows()





