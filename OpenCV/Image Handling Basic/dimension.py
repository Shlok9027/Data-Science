import cv2

img = cv2.imread('OpenCV/phase_1/python_img.png')



if img is not None:
    h, w, c = img.shape


    print(f"Loaded Successfully - \nheight : {h} \nweight : {w} \nChannnels : {c} ")


else:
    ("Unable to load the image")