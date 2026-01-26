import cv2


img_path = input('Hello User, Please Enter Your Image Path : ')


img = cv2.imread(img_path)


if img is not None:
    h, w ,c = img.shape


    show_choice = input('Hii User , Do You want to create a Line , Reactangle, Circle or text on your Image ? [line/rectangle/circle/text] : ').lower()


    if show_choice =='line':
        pt1 = (int(input("please provide x1 coordinate of point 1 : ")),int(input('please provide y1 coordinate of point 1 : ')))
        pt2 = (int(input("Please provide x2 coordinate of point 2 : ")), int(input('please provide y2 coordinate of point 2 :')))

        color = (255,123,100)

        thickness = 5
        cv2.line(img, pt1,pt2,color,thickness)
        see_choice = input("Hii User do you want to see the image ? (yes/no) ").lower()

        if see_choice == 'yes':
            cv2.line(img, pt1, pt2, color, thickness)
            cv2.imshow("Line Drawing", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        save_choice = input("Hii User now you want to save this image ? (yes/no) : ").lower()
        if save_choice == 'yes':
            save_name = input('please provide the saved img name in .png or .jpg format : ').lower()


            cv2.imwrite(save_name, img)

            print(f'Image saved successfully as {save_name}')


    if show_choice == 'rectangle':
        pt1 = (int(input("please provide x1 coordinate of point 1 : ")),int(input('please provide y1 coordinate of point 1 : ')))

        pt2 = (int(input("Please provide x2 coordinate of point 2 : ")), int(input('please provide y2 coordinate of point 2 : ')))

        color = (112,123,255)
        thickness = 4

        cv2.rectangle(img, pt1,pt2,color, thickness)
        cv2.imshow("Rectangle Drawing", img)
        see_choice = input("Hii User do you want to see the image ? (yes/no) ").lower()

        if see_choice == 'yes':
            cv2.rectangle(img, pt1, pt2, color, thickness)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

        save_choice = input("Hii User now you want to save this image ? (yes/no) : ").lower()
        if save_choice == 'yes':
            save_name = input('please provide the saved img name in .png or .jpg format').lower()

            cv2.imwrite(save_name, img)

            print(f'Image saved successfully as {save_name}')

    if show_choice == 'circle':
        center = (int(input("please provide x coordinate of center point : ")),int(input('please provide y coordinate of center point : ')))

        cv2.circle(img, center , 100, (0,0,255), 5)

        see_choice = input("Hii User do you want to see the image ? (yes/no) ").lower()

        if see_choice == 'yes':
            cv2.imshow("Circle Drawing", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        save_choice = input("Hii User now you want to save this image ? (yes/no) : ").lower()
        if save_choice == 'yes':
            save_name = input('please provide the saved img name in .png or .jpg format').lower()

            cv2.imwrite(save_name, img)

            print(f'Image saved successfully as {save_name}')

    if show_choice == 'text':
        text = input('PLease enter the text you want to write on image : ')
        position = (int(input("please provide x coordinate of text position : ")),int(input('please provide y coordinate of text position : ')))
        cv2.putText(img, text, position, cv2.FONT_HERSHEY_DUPLEX, 2,(124,244,180), 1)
        see_choice = input("Hii User do you want to see the image ? (yes/no) : ").lower()

        if see_choice == 'yes':
            cv2.imshow("Text added Drawing", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        save_choice = input("Hii User now you want to save this image ? (yes/no) : ").lower()
        if save_choice == 'yes':
            save_name = input('please provide the saved img name in .png or .jpg format : ').lower()

            cv2.imwrite(save_name, img)

            print(f'Image saved successfully as {save_name}')

else: 
    print("Unable to load the image. Please check the path and try again.")
