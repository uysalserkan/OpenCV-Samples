import cv2
import numpy as np

img1 = cv2.imread('theimage1.png')
img2 = cv2.imread('theimage2.png')

add = cv2.add(img1, img2)
add2 = img1 + img2
add3 = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow("The Image 1", add)
cv2.imshow("The Image 2", add2)
cv2.imshow("The Image 3", add3)

cv2.waitKey(0)
cv2.destroyAllWindows()
