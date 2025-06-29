# PYTHON PROGRAMS
## Hello World

Hey gang welcome to my crappy programs...

## Raspberry Pi Camera Stream

The `RasPi/camera/stream_server.py` script starts a small Flask server that
provides an MJPEG stream from the Pi camera. The page `HTML/camera_feed.html`
connects to this server and displays the live feed.

### Usage
1. Install the required packages:
   ```bash
   sudo apt install python3-flask python3-opencv
   pip install picamera2
   ```
2. Run the server on the Raspberry Pi:
   ```bash
   python3 RasPi/camera/stream_server.py
   ```
3. Open a browser on the same network and navigate to
   `http://<raspi-ip>:5000/` to see the live feed.
