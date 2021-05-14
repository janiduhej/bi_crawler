# Python program for blending of
# images using OpenCV

# import OpenCV file
import cv2
from matplotlib import pyplot as plt
from PIL import Image
# Read Image1
john = cv2.imread('./images/horse.png', 1)
kernel = cv2.getGaussianKernel(1,2)
# Gaussian Pyramid
layer = john.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

# Laplacian Pyramid
layer = gaussian_pyramid[5]
laplacian_pyramid = [layer]
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)

reconstructed_image = laplacian_pyramid[0]
for i in range(1, 6):
    size = (laplacian_pyramid[i].shape[1], laplacian_pyramid[i].shape[0])
    reconstructed_image = cv2.pyrUp(reconstructed_image, dstsize=size)
    reconstructed_image = cv2.add(reconstructed_image, laplacian_pyramid[i])
    cv2.imshow(str(i), reconstructed_image)

high_pass = cv2.GaussianBlur(reconstructed_image,(25,25),kernel, -1)
dst_john = (john/255) - high_pass
# Read image2
marylin = cv2.imread('./images/zebra.png', 1)
kernel = cv2.getGaussianKernel(1,2)
# Gaussian Pyramid
layer = marylin.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

# Laplacian Pyramid
layer = gaussian_pyramid[5]
laplacian_pyramid = [layer]
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)

low_pass = laplacian_pyramid[0]
for i in range(1, 6):
    size = (laplacian_pyramid[i].shape[1], laplacian_pyramid[i].shape[0])
    low_pass = cv2.pyrUp(low_pass, dstsize=size)
    low_pass = cv2.add(low_pass, laplacian_pyramid[i])
    cv2.imshow(str(i), low_pass)

dst = cv2.GaussianBlur(low_pass,(25,25),kernel, -1)


plt.subplot(2,2,1),plt.imshow(marylin),plt.title('Original Marylin')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(dst),plt.title('Low Pass Filter')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(john),plt.title('Original John')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(high_pass),plt.title('High Pass Filter')
plt.xticks([]), plt.yticks([])

final_image = (dst + high_pass) / 2
cv2.imwrite('final.png', final_image)
plt.show()
