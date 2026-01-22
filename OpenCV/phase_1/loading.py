import cv2


img = cv2.imread('OpenCV/phase_1/python_img.png')


if img is None:
    print("Error : Image Not Found")
else: 
    print("Image loaded Sucessfully")


    