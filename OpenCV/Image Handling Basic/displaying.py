import cv2

img = cv2.imread('OpenCV/phase_1/python_img.png')


if img is not None:
    cv2.imshow("Image showing", img)


    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:
    print('Could not load the image')
