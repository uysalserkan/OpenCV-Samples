import cv2
import numpy as np

img = cv2.imread('watch.jpeg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (255, 0, 0), 15)
cv2.rectangle(img, (15, 25), (250, 250), (0, 0, 255), 2)
cv2.circle(img, (250, 200), 85, (0, 255, 0), -1)
cv2.circle(img, (50, 20), 85, (0, 255, 255), 15)


pts = np.array([[25, 20], [50, 80], [100, 26], [
               15, 95], [54, 0], [250, 540]], np.int32)
# pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (75, 20, 180), 8)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Some TextBox", (260, 180),
            font, 3, (0, 0, 180), 1, cv2.LINE_AA)


cv2.imshow("The Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
