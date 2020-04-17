import cv2
import numpy as np


def main():

    source = cv2.imread("coins.jpg")
    gray_source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    gray_source = cv2.medianBlur(gray_source, 5)
    rows = gray_source[0]

    if gray_source is None:
        print("Error, the file cannot be found in the system..")
        return -1
    else:
        print("The gray_source is fine..")

    circles = cv2.HoughCircles(gray_source,
                               cv2.HOUGH_GRADIENT,
                               1,
                               10,
                               param1=100,
                               param2=30,
                               minRadius=5,
                               maxRadius=30)

    circles = np.round(circles[0, :]).astype('int')
    for (x, y, r) in circles:
        # center = [circle[0], circle[1]]
        cv2.circle(source, (x, x), 1, (0, 0, 255), 2)
        cv2.circle(source, (x, y), r, (255, 0, 0), 2)

    cv2.imshow("The Circles", source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()