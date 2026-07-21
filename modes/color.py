from video_capture import VideoCapture
from artist import image_to_color_ascii
import keyboard
from rich.live import Live
from rich.text import Text

def color():
    cam = VideoCapture(0)

    with Live(refresh_per_second=cam.fps) as live:
        while True:
            frame = cam.get_frame()
            live.update(Text.from_ansi(image_to_color_ascii(frame, new_width=70)))

            if keyboard.is_pressed("q"):
                break

    cam.cleanup()