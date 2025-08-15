# main.py
# Get all the tools we need
import cv2
from ultralytics import YOLO
from picamera2 import Picamera2
import time

# This function looks at one picture (a frame) and finds any people in it
def detect_humans(frame, model):
    # Tell the AI model to look for objects in the picture
    results = model(frame, stream=True, verbose=False)

    # In the AI's brain, the number for a "person" is 0
    person_class_id = 0

    # Look through everything the AI found
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Find the corners of the box to draw
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Check how sure the AI is
            confidence = box.conf[0]
            # See what object the AI thinks it is
            class_id = int(box.cls[0])

            # If the AI found a person and is pretty sure about it...
            if class_id == person_class_id and confidence > 0.5:
                # ...draw a green box around them
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # And write "Person" above the box
                label = f'Person: {confidence:.2f}'
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

# This is the main part of our program that sets everything up
def main():
    # Load the smart AI brain (YOLOv8n is a small, fast version)
    try:
        model = YOLO('yolov8n.pt')
        print("AI Brain loaded!")
    except Exception as e:
        print(f"Oops, couldn't load the AI brain: {e}")
        return

    # Turn on the camera
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": (640, 480), "format": "RGB888"})
    picam2.configure(config)
    picam2.start()
    print("Camera is on. Looking for people...")
    print("Press 'q' on the picture window to quit.")
    time.sleep(2.0) # Give the camera a second to warm up

    # This loop runs over and over
    while True:
        # Take a picture from the camera
        frame = picam2.capture_array()
        # Ask the AI to find people in the picture
        annotated_frame = detect_humans(frame, model)

        # Show the picture with the boxes on the screen
        cv2.imshow('Human Detector', annotated_frame)

        # If you press the 'q' key, stop the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean everything up
    picam2.stop()
    cv2.destroyAllWindows()
    print("Program stopped.")

# This line starts the program when you run the file
if __name__ == "__main__":
    main()