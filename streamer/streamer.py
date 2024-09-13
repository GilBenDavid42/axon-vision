from multiprocessing import Queue

import cv2

from streamer.app_settings import AppSettings
from streamer.frame_splitter import FrameSplitter


def streamer(frame_queue: Queue, video_settings_queue: Queue):
    app_settings = AppSettings()

    video_capture = cv2.VideoCapture(str(app_settings.video_path))
    video_settings_queue.put(video_capture.get(cv2.CAP_PROP_FPS))

    frame_splitter = FrameSplitter(video_capture)

    for frame in frame_splitter.split_frames():
        frame_queue.put(frame)

    frame_queue.put(None)
