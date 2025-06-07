from PIL import Image, ImageDraw

# Define the color mapping with actual RGB values
color_mapping = {
    'a': (0, 128, 0),  # green
    'b': (255, 255, 0),  # yellow
    'c': (150, 100, 150),  # purple
    'd': (255, 165, 0),  # orange
    'e': (173, 216, 230),  # light blue
    'f': (255, 182, 193),  # pink
    'g': (48, 25, 52),  # dark purple
    'h': (255, 20, 147),  # dark pink
    'i': (0, 0, 255),  # blue
    'j': ((255, 255, 255), (0, 128, 0)),  # white (top) and green (bottom)
    'k': (0, 128, 0),  # green
    'l': ((255, 255, 0), (0, 128, 0)),  # yellow (top) and green (bottom)
    'm': ((150, 100, 150), (0, 128, 0)),  # purple (top) and green (bottom)
    'n': ((255, 165, 0), (0, 128, 0)),  # orange (top) and green (bottom)
    'o': ((173, 216, 230), (0, 128, 0)),  # light blue (top) and green (bottom)
    'p': ((255, 182, 193), (0, 128, 0)),  # pink (top) and green (bottom)
    'q': ((48, 25, 52), (0, 128, 0)),  # dark purple (top) and green (bottom)
    'r': ((255, 102, 102), (0, 128, 0)),  # light red (top) and green (bottom)
    's': ((0, 0, 255), (0, 128, 0)),  # blue (top) and green (bottom)
    't': ((255, 255, 255), (255, 255, 0)),  # white (top) and yellow (bottom)
    'u': ((0, 128, 0), (255, 255, 0)),  # green (top) and yellow (bottom)
    'v': (255, 255, 0),  # yellow
    'w': ((200, 162, 200), (255, 255, 0)),  # light purple (top) and yellow (bottom)
    'x': ((255, 165, 0), (255, 255, 0)),  # orange (top) and yellow (bottom)
    'y': ((173, 216, 230), (255, 255, 0)),  # light blue (top) and yellow (bottom)
    'z': ((255, 182, 193), (255, 255, 0))  # pink (top) and yellow (bottom)
}

def create_cipher_image(input_string, output_file="cipher_image.png"):
    """
    Create a cipher image based on the input string and color mapping.

    Args:
        input_string (str): The string to encode into the image.
        output_file (str): The name of the output image file.
    """
    # Image dimensions
    cell_size = 100  # Size of each square
    width = len(input_string) * cell_size
    height = cell_size

    # Create a new image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw each character as a colored square
    for i, char in enumerate(input_string.lower()):
        x0 = i * cell_size
        y0 = 0
        x1 = x0 + cell_size
        y1 = y0 + cell_size

        # Check if the character is a "line" color
        if char in color_mapping and isinstance(color_mapping[char], tuple) and len(color_mapping[char]) == 2:
            top_color, bottom_color = color_mapping[char]
            # Draw the top half with the top color
            draw.rectangle([x0, y0, x1, y0 + cell_size // 2], fill=top_color)
            # Draw the bottom half with the bottom color
            draw.rectangle([x0, y0 + cell_size // 2, x1, y1], fill=bottom_color)
        else:
            # Draw the full square with the specified color
            color = color_mapping.get(char, (0, 0, 0))  # Default to black if char not in mapping
            draw.rectangle([x0, y0, x1, y1], fill=color)

    # Save the image
    image.save(output_file)
    print(f"Cipher image saved as {output_file}")

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to encode: ")
    create_cipher_image(user_input)