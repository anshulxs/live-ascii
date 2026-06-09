import tkinter as tk
import tkinter.font as tkfont
from PIL import ImageTk

MAX_WIDTH = 1280 
MAX_HEIGHT = 720

class Window(tk.Tk):
    def __init__(self, win_width, win_height):
        super().__init__()
        self.iconbitmap("image.ico")
        self.title("live2ascii")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        win_width = min(win_width, screen_width//2, MAX_WIDTH)
        win_height = min(win_height, screen_height, MAX_HEIGHT)

        self.font = tkfont.Font(family="Consolas", size=-10)
        self.font_width = self.font.measure("n")
        self.font_height = self.font.metrics("linespace")

        self.geometry(f"{int(win_width*2)}x{int(win_height)}")

        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(fill="both", expand=True)

        self.text_id = self.canvas.create_text(0,0, text="", fill="white", font=self.font, anchor="nw")
        self.image_id = self.canvas.create_image(win_width, 0 ,image=None, anchor="nw")
        self.photo = None

        self.resizable(False, False)

    def render(self,ascii_str, frame):
        new_photo = ImageTk.PhotoImage(frame)
        self.canvas.itemconfig(
            self.text_id,
            text=ascii_str
        )
        self.canvas.itemconfig(
            self.image_id,
            image=new_photo
        )
        self.photo = new_photo

    def run(self, loop):
        loop()
        self.mainloop()