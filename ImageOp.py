import cv2
import numpy as np

img = cv2.imread('watch.jpeg', cv2.IMREAD_COLOR)

px = img[25, 25]

print(px)

img[250, 250] = [255, 0, 255]

watch_face = img[117:166, 352:560]
img[0:235, 0:394] = watch_face

roi = img[100:150, 100:150] = [0, 0, 0]

cv2.imshow("The images", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
