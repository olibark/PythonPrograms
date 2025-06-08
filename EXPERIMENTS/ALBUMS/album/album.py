import tkinter as tk
from tkinter import simpledialog
# Approximate colours taken from your provided image (a–m on the top row, n–z on the bottom row).
# Use a colour picker on the image to get exact hex values if you want more precision.
blue_monday_cipher = {
    'A': '#F9D74B',  # yellow
    'B': '#F28A30',  # orange
    'C': '#F5AACB',  # pastel pink
    'D': '#A2DBF2',  # pastel blue
    'E': '#F2B2E2',  # lavender-pink
    'F': '#E667BF',  # pink-magenta
    'G': '#31CCE6',  # bright turquoise
    'H': '#F595C6',  # rosy pink
    'I': '#20B8C8',  # teal
    'J': '#26CEDF',  # aqua
    'K': '#53B83F',  # medium green
    'L': '#FBE53B',  # yellow
    'M': '#E3EC3B',  # yellow-lime
    'N': '#EA8333',  # deeper orange
    'O': '#28B4AA',  # greenish teal
    'P': '#CF88E0',  # light purple
    'Q': '#3FDAA7',  # mint green
    'R': '#D7E018',  # lime
    'S': '#F8D334',  # gold
    'T': '#B9B610',  # olive-gold
    'U': '#FBF541',  # bright lemon
    'V': '#00DBF9',  # bright aqua
    'W': '#F92BBF',  # bright pink
    'X': '#FAE53F',  # bright yellow
    'Y': '#FEF736',  # lemon-lime
    'Z': '#F5FA2B',  # neon yellow-lime
    ' ': '#CCCCCC'   # grey for space (adjust as needed)
}

def encode_message(message):
    # Default to grey (#CCCCCC) if a character isn’t in our cipher
    return [blue_monday_cipher.get(char.upper(), '#CCCCCC') for char in message]

def display_encoded_message(encoded_message):
    root = tk.Tk()
    root.title("Colour Cipher")

    for colour in encoded_message:
        # Use a small label with background=colour
        label = tk.Label(root, text=' ', bg=colour, width=2, height=1)
        label.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    message = simpledialog.askstring("Input", "Enter the message to encode:")
    if message:
        encoded_message = encode_message(message)
        display_encoded_message(encoded_message)