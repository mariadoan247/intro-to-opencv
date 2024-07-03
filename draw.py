# Draw/Create shapes
import cv2 as cv
import numpy as np

# Create a blank image to work with. uint8 is image data type
# Shape of height,width,numberofcolorchannels
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color.
# There will a be a red box contained in the black image
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# we'll have an outlined green rectangle starting from the origin to (250,250)
# You can fill in the rectangle by doing thickness=-1 or thickness=cv.FILLED
# Instead of fixed values like (250,250), you can do something like (blank.shape[1]//2,blank.shape[0]//2)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a Line
cv.line(blank, (100,250), (300, 400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write Text
# If the text is too long, it can get cutoff since the image cannot contain it
cv.putText(blank, 'Hello World. I am Maria!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)