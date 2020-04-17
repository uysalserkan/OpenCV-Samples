import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpeg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# ! Showing sth (img or video etc.)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ! Show and resize etc.
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()
