import numpy as np

import matplotlib.pyplot as plt

import cv2

from array import  array

import pytesseract

img = cv2.imread('Original_image.tif')

grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

upper_img = grey_img[1:85,1:280]

bottom_img = grey_img[86:145,1:280]

verify_img = grey_img[146:180,1:280]

cv2.imshow('1',upper_img)

segment_upper = list()

segment_bottom = list()

rearrange_upper = list()

rearrange_bottom = list()

rearrange_verify = list()

uplist = [11,18,15,9,2,10,5,3,4,13,20,16,12,14,7,1,6,8,27,19]

bottomlist = [16,7,18,15,3,11,10,14,4,8,5,12,20,13,19,2,1,17,9,6]

print(uplist[0])

print(range(1,21))

for i in range(1,21):
    segment_upper.append(upper_img[1:85,14*i-13:14*i])
    segment_bottom.append(bottom_img[1:60,14*i-13:14*i])


print(type(segment_bottom))

print(type(upper_img))

print(len(segment_upper))

arrangeimg_upper = []

# arrangeimg_upper = np.column_stack((segment_upper[11],segment_upper[18],segment_upper[15],segment_upper[9],segment_upper[2],segment_upper[10],segment_upper[5],segment_upper[3],segment_upper[4],segment_upper[13],segment_upper[19],segment_upper[16]))

for i in range(1,21):
    arrangeimg_upper = np.column_stack((arrangeimg_upper,segment_upper[i-1]))

cv2.imshow('11htyre',arrangeimg_upper)

cv2.waitKey(0)

