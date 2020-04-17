import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


def main():
    theQR = cv2.imread("second.png")

    decoded = pyzbar.decode(theQR)

    for obj in decoded:
        print("Type ", obj.type)
        print("Data ", obj.data, "\n")

    cv2.imshow("The QR Code", theQR)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()