from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

picam2.start()
sleep(2)  # Allow camera to adjust
picam2.capture_file("test_image.jpg")
