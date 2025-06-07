from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont
import random

def show_window(target, numberw, number2w, number3w):
    app = QApplication([])  # Create the application

    window = QWidget()  # Create the window
    window.setWindowTitle("Styled Label Window")  # Set window title
    
    # Create labels with dynamic text
    label = QLabel(f"Target: {target}", window)
    label2 = QLabel(f"Random Number 1: {numberw}", window)
    label3 = QLabel(f"Random Number 2: {number2w}", window)
    label4 = QLabel(f"Random Number 3: {number3w}", window)
    
    # Set the font to make the label text larger
    font = QFont("Arial", 40, QFont.Bold)  # Set font to Arial, size 40, bold
    label.setFont(font)
    label2.setFont(font)
    label3.setFont(font)
    label4.setFont(font)
    
    # Set label color (text color) and background color
    label.setStyleSheet("color: white; background-color: #3498db; padding: 20px;")
    label2.setStyleSheet("color: white; background-color: #e74c3c; padding: 20px;")
    label3.setStyleSheet("color: white; background-color: #2ecc71; padding: 20px;")
    label4.setStyleSheet("color: white; background-color: #f39c12; padding: 20px;")
    
    # Position the labels in the window
    label.move(100, 50)
    label2.move(100, 150)
    label3.move(100, 250)
    label4.move(100, 350)
    
    # Resize the window to accommodate the labels
    window.resize(600, 500)
    
    window.show()  # Show the window

    app.exec_()  # Start the event loop

# Generate an array of 10 random numbers between 1 and 10
array = [random.randint(1, 10) for _ in range(10)]
print("Random numbers:", array)

# Add 10 more random numbers to the array
for i in range(0, 10):
    numberi = random.randint(1, 10)
    array.append(numberi)
print("Updated array:", array)

# Select random numbers from the array
numberw = str(array[random.randint(0, len(array) - 1)])
number2w = str(array[random.randint(0, len(array) - 1)])
number3w = str(array[random.randint(0, len(array) - 1)])

# Select more random numbers for target calculation
number = array[random.randint(0, len(array) - 1)]
number2 = array[random.randint(0, len(array) - 1)]
number3 = array[random.randint(0, len(array) - 1)]

# Calculate the target
target = (number * number2 + number3)
print(f"{target} is the target")

# Pass the parameters to the show_window function
show_window(target, numberw, number2w, number3w)

