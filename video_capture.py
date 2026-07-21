import cv2
from PIL import Image

class VideoCapture:
    def __init__(self, source):
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise Exception("could not connect to camera")
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    def get_frame_width(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    def get_frame_height(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("failed to capture frame")
        flipped_frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)
        frame_img = Image.fromarray(rgb_frame)
        return frame_img

    def cleanup(self):
        self.cap.release()
        cv2.destroyAllWindows()