import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection using Canny
edges = cv2.Canny(gray, 50, 150)

# Create an output image to draw the edges on
output = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Draw the edges on the original image
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the result
cv2.imshow('Edges', output)
cv2.waitKey(0)
cv2.destroyAllWindows()