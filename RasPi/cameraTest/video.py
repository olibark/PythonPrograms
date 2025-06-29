from picamera2 import Picamera2
import cv2
import time

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)}))

camera.start()

try: 
    while True: 
        frame = camera.capture_array()
        cv2.imshow("Camera Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("Exitin")

finally: 
    cv2.destroyAllWindows()
    camera.close()
