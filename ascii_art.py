import numpy as np
from PIL import Image

ASCII_CHAR = ".:-=+*#%@"

class AsciiArt:
    def resize_image(self, image, new_width=100, font_width: float=9.6, font_height: float=16):
        font_ratio = font_height / font_width
        width, height = image.size
        aspect_ratio = height / width
        new_height = int((new_width * aspect_ratio)/font_ratio)
        resized_image = image.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
        return resized_image
    
    def img_to_greyscale(self, image):
        greyscaled_image = image.convert("L")
        return greyscaled_image
    
    def pixel_to_ascii(self, image, threshold=50, invert : bool=False):
        pixels = np.array(image)
        chars = ASCII_CHAR[::-1] if invert else ASCII_CHAR
        ascii_art = []
        for pixel in pixels.flatten():
            if pixel < threshold:
                ascii_art.append(" ")
            else:
                ascii_art.append(chars[pixel // 32])
        return "".join(ascii_art)
    
    def pixel_to_color_ascii(self, image):
        pixels = np.array(image).flatten()
        color_code = '\033[38;2;{R};{G};{B}m{text}\033[0m'
        color_ascii_art = []
        for i in range(0, len(pixels)-2, 3):
            color_char = color_code.format(R=pixels[i], G=pixels[i+1], B=pixels[i+2], text="@")
            color_ascii_art.append(color_char)
        return color_ascii_art

    def image_to_ascii(self, image, new_width=100, threshold=50, font_width: float=9.6, font_height: float=16, invert=False):
        resized_image = self.resize_image(image, new_width, font_width, font_height)
        grayscaled_image = self.img_to_greyscale(resized_image)
        ascii_str = self.pixel_to_ascii(grayscaled_image, threshold, invert)
        ascii_image = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
        return "\n".join(ascii_image)
    
    def image_to_color_ascii(self, image, new_width=100, font_width: int=8, font_height: int=16):
        resized_image = self.resize_image(image, new_width, font_width, font_height)
        ascii_str = self.pixel_to_color_ascii(resized_image)
        ascii_image = ["".join(ascii_str[i:i+new_width]) for i in range(0, len(ascii_str), new_width)]
        return "\n".join(ascii_image)