import cv2

img = cv2.imread('OpenCV/Imagr Drawing function/doddlify_img.png')  


if img is None:
    print("Image Not Found")

else:
    print("Image Loaded Successfully")


    pt1 = (50,150)

    pt2 = (300,500)

    color = (255,0,255)

    thickness = 5

    cv2.line(img, pt1, pt2, color, thickness)
    cv2.imshow("Line Drawing", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()