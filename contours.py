# Countours are the boundaries of objects.
# Not the same as edges in a mathematical point of view.
# Countours are useful tools when you get into shape analysis, object detection, and recognition
# From a programming point of view you can get away with thinking of contours as edges
# Recommend: Use the canny images to find the contours instead of the threshold method
import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat4.jpg')
cv.imshow('Cats', img)

# Create a blank image to draw on and visulaize the contours
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur the grayed image. This will decrease the number of contours significantly.
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Grab the edges of the blurred grayed image using the canny edge detector
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Thresholding basically tries to binarize an image. If a particular pixel is below 125 it will be set to 0/black. above 125 will be set to white/255
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Find the countours
# Returns Countours and hierarchies
# cv.RETR_LIST returns all of the contours, RETR_EXTERNAL returns external contours, RETR_TREE returns all the hierarchical contours
# This method will look at the structuring element and will return two values
# contours: List of all the coordinates of the contours found in the image
# hierarchies: Refers to the hierarchical representation of the contours (squares, rectangles, etc.)
# The contour approximation method is how we want to approximate the contours.
# CHAIN_APPROX_NONE will just return all the contour coordinates. SIMPLE will compress the contours into endpoints only.
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# We can find the number of contours that were found by finding the length of the contours list
print(f'{len(contours)} contour(s) found!')

# Draw the contours on the blank image so we can see what kind of contours were found
# -1 indicates that we want all the contours to be drawn
# (0,0,255) --> red
# 1 --> thickness
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)