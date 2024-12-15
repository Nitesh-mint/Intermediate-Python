from PIL import Image
import numpy as np

# ASCII characters used to represent pixels
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize the image and convert it to grayscale
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    grayscale_image = image.convert("L")  # Convert to grayscale
    pixels = np.array(grayscale_image)
    ascii_str = ""
    for pixel_row in pixels:
        for pixel in pixel_row:
            ascii_str += ASCII_CHARS[pixel // 25]  # Choose ASCII character
        ascii_str += "\n"
    return ascii_str

# Generate SVG <tspan> elements from the ASCII art
def ascii_to_svg(ascii_str):
    lines = ascii_str.splitlines()
    svg_content = '<text>\n'
    y_position = 30
    for line in lines:
        svg_content += f'<tspan x="15" y="{y_position}">{line}</tspan>\n'
        y_position += 20  # Adjust y_position for each line
    svg_content += '</text>'
    return svg_content

# Main function to convert image to SVG
def image_to_svg(image_path, new_width=100):
    image = Image.open(image_path)
    resized_image = resize_image(image, new_width)
    ascii_str = pixels_to_ascii(resized_image)
    svg_output = ascii_to_svg(ascii_str)
    return svg_output

# Path to your image
image_path = '/Users/niteshmint/Downloads/my_close.jpeg'

# Convert the image and print the SVG output
svg_output = image_to_svg(image_path)


with open("my_ascii_art.svg","w") as f:
    f.write(svg_output)