# Get the special camera tools ready to use
from picamera2 import Picamera2, Preview
import time

try:
    # Wake up the camera
    print("Turning camera on...")
    picam2 = Picamera2()

    # Get the preview window ready
    preview_config = picam2.create_preview_configuration()
    picam2.configure(preview_config)

    # Show the preview window on the screen
    print("Starting preview...")
    picam2.start_preview(Preview.QTGL)

    # Start the camera feed
    picam2.start()
    print("Camera is live! Press Ctrl+C in the terminal to stop.")

    # Keep the program running so the window stays open
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # This part runs when you press Ctrl+C
    print("\nOkay, stopping the camera.")

finally:
    # This part makes sure the camera always turns off safely
    print("Closing window and turning camera off...")
    picam2.stop_preview()
    picam2.stop()
    print("All done. Goodbye!")