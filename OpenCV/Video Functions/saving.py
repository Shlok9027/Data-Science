import cv2

camera = cv2.VideoCapture(0)

frame_width  = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))


frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


codec = cv2.VideoWriter.fourcc(*'XVID')

recorder = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))


while True:

    success, image = camera.read()


    if not success:
        print("Failed to grab frame")
        break

    recorder.write(image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")

        break

camera.release()

recorder.release()
cv2.destroyAllWindows()