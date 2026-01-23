import cv2

img = cv2.imread('OpenCV/Image Drawing function/doddlify_img.png')

if img is None:
    print("Image Not Found")


else:
    print("Image Loaded Successfully")


    pt1 = (50,50)

    pt2 = (350,400)

    color = (0,255,0)


    thickness = 3


    cv2.rectangle(img, pt1, pt2, color, thickness)


    cv2.imshow("Rectangle Drawing", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 