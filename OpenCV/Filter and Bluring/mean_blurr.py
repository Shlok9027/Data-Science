import cv2

img = cv2.imread('OpenCV/nature.jpg')


resized_img = cv2.resize(img,(800,600))

mean_blurred_img  = cv2.medianBlur(resized_img,11)

cv2.imshow("Original Image", resized_img)

cv2.imshow("Mean Blue Image", mean_blurred_img )

cv2.waitKey(0)

cv2.destroyAllWindows()