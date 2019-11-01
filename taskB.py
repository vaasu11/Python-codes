import numpy
import cv2
img1=cv2.imread('cat.jpg')



r = img1.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0
cv2.imshow('image',r)
cv2.imwrite('cat_red.jpg',r)
