import cv2


img = cv2.imread('OpenCV/Image Resizing/doddlify_img.png')


if img is None:
    print("Imae Not Found")



else:
    flipped_horizonal = cv2.flip(img, 1)
    flipped_vertical = cv2.flip(img, 0)
    flipped_both = cv2.flip(img, -1)

    cv2.imshow("OriginalImage", img)
    cv2.imshow("Horizontal Image ", flipped_horizonal)
    cv2.imshow("Vertical Image ", flipped_vertical)
    cv2.imshow("Both Image ", flipped_both)

    cv2.waitKey(0)

    cv2.destroyAllWindows