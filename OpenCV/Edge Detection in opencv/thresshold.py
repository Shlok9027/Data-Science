import cv2

img = cv2.imread('OpenCV/man.png', cv2.IMREAD_GRAYSCALE)


resize_img = cv2.resize(img, (600, 400))

ret, thresshold_img = cv2.threshold(resize_img, 100, 255, cv2.THRESH_BINARY)


cv2.imshow('Original Image', resize_img)

cv2.imshow('Thresshhold Image', thresshold_img)


cv2.waitKey(0)

cv2.destroyAllWindows()