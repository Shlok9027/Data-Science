import cv2 


face_Cascade = cv2.CascadeClassifier('OpenCV\Face and Object Detetction\haarcascade_frontalface_default.xml',)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_Cascade.detectMultiScale(gray, 1.1, 5)

    '''
    detectMultiScale() - scan and detect faces
    1.1 - balance, not too slow , blind

    minNeighbors - how many objects are detected near the current one to consider it a face
    5 - good value 
    '''

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y) , (x+w, y+h), (123,231,12),4)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows() 
