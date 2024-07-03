import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat2.jpeg')

cv.imshow('cat4', img)


# Translation
# Shifting the image along the x and y axis (up, down, left, right)
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# +x --> right
# +y --> down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)


# Rotation
# OopenCV let's you specify any rotation point you want
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    # Default is center
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# Positive angle rotates counter clockwise and negative rotates clockwise
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Rotating the rotated will add extra black sections.
# Add the two angle values to prevent this (-45 + -45 = -90)
rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
# flipcode: 0 -> flip vertical, 1 -> flip horizontally, -1 -> flip both ways
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)