import cv2
import numpy as np

capture = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.mp4", -1, 25.0, (640, 480))

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    cv2.imshow('Capturing Frame', frame)
    cv2.imshow('Capturing Gray Frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()
