import cv2

img = cv2.imread('OpenCV/Image Resizing/doddlify_img.png')


if img is not None:
    cropeed_img = img[100:200, 50:150]

    cv2.imshow("Original Image" , img)
    cv2.imshow("Cropped Image", cropeed_img)


    cv2.waitKey(0)

    cv2.destroyAllWindows()

    