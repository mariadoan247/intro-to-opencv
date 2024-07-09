import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat4.jpg')
cv.imshow('Cat', img)

# Display what the img will look like outside of the openCV way
# OpenCV displays as BGR because the image is BGR. matplotlib doesn't know that it's
# a BGR image and instaed displays it as an rgb image.
# plt.imshow(img)
# plt.show()

# Convert BGR (Blue Green Red) image to Grayscale 
# Grayscale cannot be directly converted to HSV/LAB and vice versa
# You would have to convert grayscale back to bgr first
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Convert BGR image to HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR --> Lab (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR --> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
# You'll notice now plt displays the rgb image as the og bgr image
# plt.imshow(rgb)
# plt.show()

# HSV --> BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)
# LAB --> BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_HSV2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)