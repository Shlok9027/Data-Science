import cv2

img = cv2.imread('OpenCV/phase_1/python_img.png')


if img is not None:

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    cv2.imshow("Gray_Img" , gray)


    cv2.waitKey(0)

    cv2.destroyAllWindows()


    save = cv2.imwrite("gray_img.png", gray)

else:
    print("Unable to load the image ")