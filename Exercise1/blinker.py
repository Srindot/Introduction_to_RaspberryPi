from gpiozero import LED
from time import sleep

# Tell the Pi that our LED is connected to pin 17
led = LED(17)

print("Starting the blinker... Press Ctrl+C to stop.")

try:
    # This loop will run forever
    while True:
        led.on()    # Turn the light on
        sleep(1)    # Wait for 1 second
        led.off()   # Turn the light off
        sleep(1)    # Wait for 1 second
except KeyboardInterrupt:
    print("\nStopping the program.")