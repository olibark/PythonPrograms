from flask  import Flask, Response
from picamera2 import Picamera2
import cv2

running = True

app = Flask(__name__)

camera = Picamera2()
configuration = camera.create_video_configuration(
    main={"size": (2304, 1296), "format": "RGB888"}
)

camera.configure(configuration)
camera.start()

def captureFrames():
    while running:
        frame = camera.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        frameBytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frameBytes + b'\r\n')
        
@app.route('/video_feed')
def videoFeed():
    return Response(captureFrames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)