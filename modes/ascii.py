from artist import image_to_ascii
from video_capture import VideoCapture
from rich.live import Live
from rich.text import Text
import keyboard

def ascii():
    cam = VideoCapture(0)
    
    with Live(refresh_per_second=cam.fps) as live:
        while True:
            frame = cam.get_frame()
            ascii_image = image_to_ascii(frame, new_width=70)
            live.update(Text(ascii_image))

            if keyboard.is_pressed("q"):
                break

    cam.cleanup()