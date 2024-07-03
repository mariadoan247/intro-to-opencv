import cv2 as cv

img = cv.imread('Photos/dog1.jpeg')
cv.imshow('Cat', img)

# Converting an image to grayscale.
# #Allows us to see the intensity of the pixels instead of just the color.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
# Removes some of the extra noise in an image
# The kernel size determines how blurry the image will be. Smaller is less blurred.
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# Multi-step process involving blurring and gridding etc.
# You can reduce the number of edges outlined by blurring the image.
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the Image
# Uses the structuring image canny to dilate it based on a kernel size
# The differences are subtle. Lines will thicken or features become more prominent.
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
# There is a subtle change in the edges and the thickness
# You can match the kernel and the iterations to (in most cases) get back the same edge cascade
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
# The interpolation's default is usually used when trying to make an image smaller.
# If you want to make the image bigger, then you would add an interpolation.
# INTER_CUBIC is the slower one, but often results in better quality.
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)