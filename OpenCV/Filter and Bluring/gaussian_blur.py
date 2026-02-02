import cv2

img = cv2.imread('OpenCV/nature.jpg')

resized_img = cv2.resize(img, (800, 600))
blurred_img = cv2.GaussianBlur(resized_img, (5, 5), 3)

cv2.imshow("Original Image", resized_img)
cv2.imshow("Blurred Img", blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
