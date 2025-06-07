import tkinter as tk
from tkinter import simpledialog

blue_monday_cipher = {
    'A': '#FF5733',  # red
    'B': '#33FF57',  # green
    'C': '#3357FF',  # blue
    'D': '#FF33A1',  # pink
    'E': '#A133FF',  # purple
    'F': '#33FFA1',  # teal
    'G': '#FFA133',  # orange
    'H': '#A1FF33',  # lime
    'I': '#33A1FF',  # sky blue
    'J': '#FF5733',  # red
    'K': '#33FF57',  # green
    'L': '#3357FF',  # blue
    'M': '#FF33A1',  # pink
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

def decode_message(encoded_message):
    # Reverse the cipher dictionary
    reversed_cipher = {v: k for k, v in blue_monday_cipher.items()}
    # Default to space (' ') if a colour isn’t in our reversed cipher
    return ''.join([reversed_cipher.get(colour, ' ') for colour in encoded_message])

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
        decoded_message = decode_message(encoded_message)
        print("Decoded message:", decoded_message)

    encoded_message = simpledialog.askstring("Input", "Enter the encoded message (comma-separated hex values):")
    if encoded_message:
        encoded_message_list = encoded_message.split(',')
        decoded_message = decode_message(encoded_message_list)
        print("Decoded message:", decoded_message)