import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobalx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobaly = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 100)

    cv2.imshow("Default", frame)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("X", sobalx)
    cv2.imshow("Y", sobaly)
    cv2.imshow("Edges", edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
