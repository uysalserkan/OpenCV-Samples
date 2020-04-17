import cv2
import numpy as np


def main():
    pixels = np.zeros((500, 500, 3), dtype="uint8")

    cv2.circle(pixels, (250, 250), 100, (0, 150, 250), 1)
    cv2.rectangle(pixels, (150, 150), (350, 350), (150, 0, 250), 1)
    cv2.line(pixels, (150, 150), (350, 350), (250, 250, 250), 1)
    cv2.line(pixels, (150, 350), (350, 150), (250, 250, 250), 1)
    cv2.line(pixels, (250, 150), (250, 350), (250, 250, 250), 1)
    cv2.line(pixels, (150, 250), (350, 250), (250, 250, 250), 1)

    cv2.imshow("The Board", pixels)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()