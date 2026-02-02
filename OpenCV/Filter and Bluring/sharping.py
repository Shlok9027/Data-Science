import cv2
import numpy as np

img = cv2.imread('OpenCV/nature.jpg')

resized_img = cv2.resize(img, (800, 600))

sharpen_kernal = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpned_img = cv2.filter2D(resized_img, -1, sharpen_kernal)

cv2.imshow("Original Image", resized_img)
cv2.imshow("Sharpned Image", sharpned_img)

cv2.waitKey(0)

cv2.destroyAllWindows()