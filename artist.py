import numpy as np
from PIL import Image
import cv2

ASCII_CHAR = '  .-:=+*#%@'


def resize_image(image, new_width=70, font_width: float=9.6, font_height: float=16):
    font_ratio = font_height / font_width
    width, height = image.size
    aspect_ratio = height / width
    new_height = int((new_width * aspect_ratio)/font_ratio)
    resized_image = image.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
    return resized_image

def img_to_greyscale(image):
    greyscaled_image = image.convert("L")
    return greyscaled_image

def canny_edge_detection(image, low_thresh=80, high_thresh=170):
    gray = np.array(image)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blurred, threshold1=low_thresh, threshold2=high_thresh)
    return edges

def pixel_to_ascii(image, invert: bool=False):
    pixels = np.array(image)
    chars = ASCII_CHAR[::-1] if invert else ASCII_CHAR
    ascii_art = []
    for pixel in pixels.flatten():
        ascii_art.append(chars[pixel // 25])
    return "".join(ascii_art)

def pixel_to_color_ascii(image):
    pixels = np.array(image).flatten()
    color_code = '\033[38;2;{R};{G};{B}m@\033[0m'
    color_ascii_art = []
    for i in range(0, len(pixels)-2, 3):
        color_char = color_code.format(R=pixels[i], G=pixels[i+1], B=pixels[i+2])
        color_ascii_art.append(color_char)
    return color_ascii_art

def pixel_to_edges(image):
    edges_str = []
    edges = canny_edge_detection(image).flatten()
    for i in range(len(edges)):
        if edges[i] == 255:
            edges_str.append(" ")
        else:
            edges_str.append(".")
    return "".join(edges_str)

def image_to_ascii(image, new_width=70, font_width: float=8, font_height: float=16, invert=False):
    resized_image = resize_image(image, new_width, font_width, font_height)
    grayscaled_image = img_to_greyscale(resized_image)
    ascii_str = pixel_to_ascii(grayscaled_image, invert)
    ascii_image = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
    return "\n".join(ascii_image)

def image_to_color_ascii(image, new_width=70, font_width: float=8, font_height: float=16):
    resized_image = resize_image(image, new_width, font_width, font_height)
    ascii_str = pixel_to_color_ascii(resized_image)
    ascii_image = ["".join(ascii_str[i:i+new_width]) for i in range(0, len(ascii_str), new_width)]
    return "\n".join(ascii_image)

def image_to_edges(image, new_width=70, font_width: float=8, font_height: float=16):
    resized_image = resize_image(image, new_width, font_width, font_height)
    grayscaled_image = img_to_greyscale(resized_image)
    edges = pixel_to_edges(grayscaled_image)
    edges_image = [edges[i:i+new_width] for i in range(0, len(edges), new_width)]
    return "\n".join(edges_image)