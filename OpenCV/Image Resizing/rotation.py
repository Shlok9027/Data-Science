import cv2

img = cv2.imread('OpenCV/Image Resizing/doddlify_img.png')


if img is None:
    print("Could not load Image")

else:
     (h, w) = img.shape[:2]

     center = (w//2, h//2)


     M = cv2.getRotationMatrix2D(center, 90, 1.0)

     rotated = cv2.warpAffine(img, M, (w, h))

     cv2.imshow("Original", img)

     cv2.imshow("Rotated", rotated)

     cv2.waitKey(0)
     cv2.destroyAllWindows() 