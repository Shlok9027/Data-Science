import cv2


img  = cv2.imread('OpenCV/flower.png', cv2.IMREAD_GRAYSCALE)
resized_img = cv2.resize(img, (600, 400))
edges = cv2.Canny(resized_img, 50, 150)


cv2.imshow("Original Image", resized_img)
cv2.imshow("Canny Edges" , edges)

cv2.waitKey(0)

cv2.destroyAllWindows() 