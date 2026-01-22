import cv2


image_path = input("Hello User , PLease provide your image address : ")
img = cv2.imread(image_path)



if img is not None:

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    h, w, c = img.shape

    show_choice = input("Hii User do you want to see the image ? (yes/no) ").lower()

    if show_choice == "yes":
        cv2.imshow(f"Gray Color Image-  height: {h} , widht: {w}, Channel: {c}  ", gray)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


    save_choice = input("Hii User now you want to save this image ? (yes?no)").lower()


    if save_choice == 'yes':
        save_name = input("please provide the saved image name with (.png, .jpg)").lower()

        cv2.imwrite(save_name,gray)

        print(f"Image saved successfully as {save_name} ")
    
else:
    print("unable to load the image")

