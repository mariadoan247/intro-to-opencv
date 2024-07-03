# Rescales a large image or video
import cv2 as cv

# img = cv.imread('Photos/cat4.jpg')
# cv.imshow('Cat', img)

# Works for images, videos, and live videos
def rescaleFrame(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)

# Only works with live videos
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


## Reading Videos
# Either takes in integer arguments or a path to a video file. Integer is if you are using your webcam or a camera that is connected to your computer.
# We'll be reading from a filepath
capture = cv.VideoCapture('Videos/cat1.mp4')

# Read the video frame by frame by utilizing the capture.read method. It is displayed with imshow. The while loop will be broken when the letter d is pressed.
# You get the cv2.error because frames ran out and the window will close automatically.
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)