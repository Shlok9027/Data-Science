import cv2

img = cv2.imread('OpenCV/Image Drawing function/doddlify_img.png')

if img is None:
    print("Image Not Found")


else:
    print("Image Loaded Successfully")

    cv2.circle(img, (250,200), 100,(233,0,123),5 )
    



    cv2.imshow("circle Drawing", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 