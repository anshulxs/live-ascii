from ascii_art import AsciiArt
from video_capture import VideoCapture
from window import Window

def main():
    cap = VideoCapture(0)
    frame_width = cap.get_frame_width()
    frame_height = cap.get_frame_height()
    window = Window(frame_width, frame_height)

    def loop():
        frame = cap.get_frame()
        ascii_art = AsciiArt(frame)
        ascii_str = ascii_art.image_to_ascii((window.winfo_width()//2)//window.font_width,
                                              90,
                                              font_width=window.font_width,
                                              font_height=window.font_height,
                                              )
        window.render(ascii_str, frame)
        window.after(int(1000//cap.fps), loop)

    window.run(loop)
    cap.cleanup()

if __name__ == '__main__':
    main()
