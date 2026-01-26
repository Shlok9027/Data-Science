import cv2

img = cv2.imread('OpenCV/Image Drawing function/doddlify_img.png')

if img is None:
    print("Image Not Found")


else:
    print("Image Loaded Successfully")

    cv2.putText(img, 'Hello Data Analytics',(100,400), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,255,124), 2 )
    cv2.imshow("Text Drawing", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 