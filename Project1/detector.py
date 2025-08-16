# flask_app.py
from flask import Flask, Response
import cv2
from ultralytics import YOLO
from picamera2 import Picamera2
import time

# Load YOLO model once
model = YOLO("yolov8n.pt")

# Init Flask app
app = Flask(__name__)

# Start camera once
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480), "format": "RGB888"})
picam2.configure(config)
picam2.start()
time.sleep(2.0)  # warmup

# Function to detect humans (your same code)
def detect_humans(frame, model):
    results = model(frame, stream=True, verbose=False)
    person_class_id = 0
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = box.conf[0]
            class_id = int(box.cls[0])
            if class_id == person_class_id and confidence > 0.5:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"Person: {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

# Generator for streaming frames
def gen_frames():
    while True:
        frame = picam2.capture_array()
        frame = detect_humans(frame, model)

        # Convert to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()

        # Stream to browser
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "<h2>YOLO Human Detection</h2><img src='/video_feed'>"

if __name__ == "__main__":
    print("Starting Flask server at http://0.0.0.0:5000/")
    app.run(host="0.0.0.0", port=5000, debug=False)
