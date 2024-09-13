from typing import Generator

import cv2
from numpy import ndarray


class FrameSplitter:
    def __init__(self, video_capture: cv2.VideoCapture):
        self.video_capture = video_capture

    def split_frames(self) -> Generator[ndarray, None, None]:
        """
        Yields video_capture frames until there are no more frames
        :return: Generator of numpy ndarray frames
        """
        next_frame_exists = True
        while next_frame_exists:
            next_frame_exists, frame = self.video_capture.read()
            yield frame
