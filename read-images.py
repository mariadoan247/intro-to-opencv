import cv2 as cv

# Read in images. Basically takes a path to image and returns that as a matrix of pixels
img = cv.imread('Photos/cat4.jpg')

# Display the image as a new window. Pass in the name of the window and the matrix of pixes to display
cv.imshow('Cat', img)

# Keyboard binding function. Waits for a specific delay for a keyboard key to be pressed.
cv.waitKey(0) 


