from pathlib import Path

import cv2


class FrameSplitter:
    def __init__(self, video_path: Path):
        self.video_path = video_path

    def split_frames(self):
        cap = cv2.VideoCapture(self.video_path)
        next_frame_exists = True
        while next_frame_exists:
            next_frame_exists, frame = cap.read()
            yield frame
