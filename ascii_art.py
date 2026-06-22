import numpy as np

ASCII_CHAR = " .:-=+*#%@"

class AsciiArt:
    def __init__(self, image):
        self.image = image

    def resize_image(self,new_width=100, font_width=None, font_height=None):
        font_ratio = 2.4
        if font_width and font_height:
            font_ratio = font_height / font_width
        width, height = self.image.size
        aspect_ratio = height / width
        new_height = int((new_width * aspect_ratio)/font_ratio)
        self.image = self.image.resize((new_width, new_height))
    
    def img_to_greyscale(self):
        self.image = self.image.convert("L")
    
    def pixel_to_ascii(self, threshold=50, invert : bool=False):
        pixels = np.array(self.image)
        chars = ASCII_CHAR[::-1] if invert else ASCII_CHAR
        ascii_art = []
        for pixel in pixels.flatten():
            if pixel < threshold:
                ascii_art.append(" ")
            else:
                ascii_art.append(chars[pixel // 32])
        return "".join(ascii_art)

    def image_to_ascii(self, new_width=100, threshold=50, invert=False, font_width=None, font_height=None):
        self.resize_image(new_width, font_width, font_height)
        self.img_to_greyscale()
        ascii_str = self.pixel_to_ascii(threshold, invert)
        ascii_image = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
        return "\n".join(ascii_image)