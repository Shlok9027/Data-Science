import cv2

img = cv2.imread('OpenCV/Image Resizing/doddlify_img.png')



if img is None:
    print("Image Not Found")


else:
    print("Image Loadede Successfully")


    resized_img  = cv2.resize(img, (300,300))

    cv2.imshow("Resized Image ", resized_img)

    cv2.imwrite("resized_output.png", resized_img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()