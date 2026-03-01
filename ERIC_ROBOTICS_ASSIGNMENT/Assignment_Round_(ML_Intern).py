import cv2
import time
from ultralytics import YOLO

#  Loading the pretrained YOLO model
# Using yolov8n because its lightweight and runs faster on normal systems.
model = YOLO('yolov8n.pt') 

# Starting the webcam (camera index 0 usually means default camera)
cam = cv2.VideoCapture(0)

#  Dictionary for required objects in this assignment
# we are mapping similar looking objects for testing purpose.
target_map = {
    "stop sign": 0.75,      
    "traffic light": 0.6,   
    "person": 1.7,          
    "bench": 0.5,           
    "bottle": 0.25          
}

# Focal length value (assumed). Ideally it should be calibrated,
# but for this assignment we are using fixed value.
focal_length = 800 

print("System Active. Looking for Navigation Objects...")

while True:
    # Starting timer to calculate FPS
    start_time = time.time()

    # Reading frame from camera
    success, frame = cam.read()
    if not success:
        break

    # Running object detection on current frame
    # Model gives bounding boxes, class ids and confidence
    results = model(frame, verbose=False)[0]

    for box in results.boxes:
        # Getting class id predicted by model
        class_id = int(box.cls[0])

        # Getting class name from model names list
        detected_name = model.names[class_id]
        
        # Only process objects which are relevant for navigation
        # Ignore other random detections
        if detected_name in target_map:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Calculating height of bounding box in pixels
            pixel_height = y2 - y1
            
            # Distance estimation using simple pinhole camera formula
            # Distance = (Real Height × Focal Length) / Pixel Height
            real_h = target_map[detected_name]
            distance = round((real_h * focal_length) / pixel_height, 2)

            # Renaming classes to match assignment wording
            # Bench is displayed as Barrier
            # Traffic light shown as Cone/Sign
            display_name = detected_name
            if detected_name == "bench":
                display_name = "Barrier"
            if detected_name == "traffic light":
                display_name = "Cone/Sign"

            # Drawing bounding box around detected object
            color = (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Writing object name and estimated distance above box
            cv2.putText(
                frame,
                f"{display_name.capitalize()}, {distance}m",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    # Calculating Frames Per Second to check performance
    fps = int(1 / (time.time() - start_time))

    # Displaying FPS on screen
    cv2.putText(
        frame,
        f"FPS: {fps}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,0,255),
        2
    )

    # Showing output window
    cv2.imshow("Robotics Detection System", frame)

    # Press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Releasing camera and closing all windows
cam.release()
cv2.destroyAllWindows()