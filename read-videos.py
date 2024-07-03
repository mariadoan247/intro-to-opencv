import cv2 as cv

## Reading Videos
# Either takes in integer arguments or a path to a video file. Integer is if you are using your webcam or a camera that is connected to your computer.
# We'll be reading from a filepath
capture = cv.VideoCapture('Videos/cat1.mp4')

# Read the video frame by frame by utilizing the capture.read method. It is displayed with imshow. The while loop will be broken when the letter d is pressed.
# You get the cv2.error because frames ran out and the window will close automatically.
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

