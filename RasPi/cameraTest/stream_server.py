from flask import Flask, Response
from picamera2 import Picamera2
import cv2

app = Flask(__name__, static_folder='../../HTML')

camera = Picamera2()
camera.configure(camera.create_video_configuration(main={"format": "RGB888", "size": (640, 480)}))
camera.start()


def gen_frames():
    while True:
        frame = camera.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return app.send_static_file('camera_feed.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
