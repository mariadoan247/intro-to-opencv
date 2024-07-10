import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat4.jpg')
cv.imshow ('Cat', img)



cv.waitKey(0)