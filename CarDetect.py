import cv2
import numpy as np


def main():
    cars = cv2.CascadeClassifier("cars.xml")
    video1 = cv2.VideoCapture("video1.avi")
    video2 = cv2.VideoCapture("video2.avi")
    video3 = cv2.VideoCapture("video3.mp4")

    while True:
        ret1, cap1 = video1.read()
        ret2, cap2 = video2.read()
        ret3, cap3 = video3.read()

        theCars1 = cars.detectMultiScale(cap1, 1.1, 3)
        for (x, y, w, h) in theCars1:
            cv2.rectangle(cap1, (x, y), (x + w, y + h), (255, 0, 0), 3)

        theCars2 = cars.detectMultiScale(cap2, 1.1, 3)
        for (x, y, w, h) in theCars2:
            cv2.rectangle(cap2, (x, y), (x + w, y + h), (255, 0, 0), 3)

        theCars3 = cars.detectMultiScale(cap3, 1.1, 3)
        for (x, y, w, h) in theCars3:
            cv2.rectangle(cap3, (x, y), (x + w, y + h), (255, 0, 0), 3)

        cv2.imshow("Video-3", cap3)
        cv2.imshow("Video-2", cap2)
        cv2.imshow("Video-1", cap1)

        k = cv2.waitKey(25) & 0xff
        if k == 27:
            break


if __name__ == "__main__":
    main()

    # ! Üst görüntü olan Video3 için doğru çalışmıyor.