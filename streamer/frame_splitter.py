import cv2


class FrameSplitter:
    def __init__(self, video_capture: cv2.VideoCapture):
        self.video_capture = video_capture

    def split_frames(self):
        next_frame_exists = True
        while next_frame_exists:
            next_frame_exists, frame = self.video_capture.read()
            yield frame
