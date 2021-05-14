from __future__ import print_function
from __future__ import division
import cv2 as cv
import argparse
alpha_slider_max = 100
title_window = 'Low Filter Blend'
def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
    cv.imshow(title_window, dst)
parser = argparse.ArgumentParser(description='Code for Adding a Trackbar to our applications tutorial.')
parser.add_argument('--input1', help='Path to the first input image.', default='avatar.jpg')
parser.add_argument('--input2', help='Path to the second input image.', default='avatar_blur.jpg')
parser.add_argument('--input3', help='Path to the third input image.', default='avatar_box.jpg')
parser.add_argument('--input4', help='Path to the fourth input image.', default='avatar_gaussian_blur.jpg')
parser.add_argument('--input5', help='Path to the fifth input image.', default='avatar_bilateral.jpg')

args = parser.parse_args()
src1 = cv.imread(cv.samples.findFile(args.input1))
src2 = cv.imread(cv.samples.findFile(args.input2))
src3 = cv.imread(cv.samples.findFile(args.input3))
src4 = cv.imread(cv.samples.findFile(args.input4))
src5 = cv.imread(cv.samples.findFile(args.input5))

if src1 is None:
    print('Could not open or find the image: ', args.input1)
    exit(0)
if src2 is None:
    print('Could not open or find the image: ', args.input2)
    exit(0)
if src3 is None:
    print('Could not open or find the image: ', args.input3)
    exit(0)
if src4 is None:
    print('Could not open or find the image: ', args.input4)
    exit(0)
if src5 is None:
    print('Could not open or find the image: ', args.input5)
    exit(0)
cv.namedWindow(title_window)
trackbar_name = 'Alpha x %d' % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
# Show some stuff
on_trackbar(0)
# Wait until user press some key
cv.waitKey()
