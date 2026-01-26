# import cv2


# cam = cv2.VideoCapture(0)

# frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


# codec = cv2.VideoWriter.fourcc(*'XVID')

# recorder = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))



# while True:


#     success, frame = cam.read()


#     if not success:
#         print("Failed to grab frame")
#         break


#     show_choice = input("Hii User do you want to record the video or save the video ? (record/save ) : ").lower()


#     if show_choice =='record':

#         cv2.imshow("WebCam Starting...", frame)

#         if cv2.waitKey(1) & 0xFF ==ord('q'):
#             print("Quitting...")
#             break

#     if show_choice == 'save':

#         recorder.write(frame)

#         print("Recording video... Press 'q' to stop.")
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             print("Quitting...")
#             break
# cam.release()
# recorder.release()

# cv2.destroyAllWindows()


import cv2

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter.fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))

while True:

    success, frame = cam.read()

    if not success:
        print("Failed to grab frame")
        break

    show_choice = input(
        "Hii User do you want to record the video or save the video ? (record/save ) : "
    ).lower()

    if show_choice == 'record':

        cv2.imshow("WebCam Starting...", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break

    if show_choice == 'save':

        cv2.imshow("WebCam Starting...", frame)   # 🔹 FIX: show camera window
        recorder.write(frame)

        print("Recording video... Press 'q' to stop.")
        if cv2.waitKey(1) & 0xFF == ord('q'):      # 🔹 FIX: waitKey (case-sensitive)
            print("Quitting...")
            break

cam.release()
recorder.release()
cv2.destroyAllWindows()
