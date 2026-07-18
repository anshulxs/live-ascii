from ascii_art import AsciiArt
from video_capture import VideoCapture
from rich.live import Live
import keyboard

def ascii():
    cam = VideoCapture(0)
    artist = AsciiArt()
    
    with Live(refresh_per_second=cam.fps) as live:
        while True:
            frame = cam.get_frame()
            ascii_image = artist.image_to_ascii(frame, new_width=70)
            live.update(ascii_image)

            if keyboard.is_pressed("q"):
                break

    cam.cleanup()