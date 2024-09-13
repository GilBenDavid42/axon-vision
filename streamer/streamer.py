from multiprocessing import Queue

from project.streamer.app_settings import AppSettings
from streamer.frame_splitter import FrameSplitter


def streamer(frame_queue: Queue):
    app_settings = AppSettings()
    frame_splitter = FrameSplitter(app_settings.video_path)
    for frame in frame_splitter.split_frames():
        frame_queue.put(frame)
