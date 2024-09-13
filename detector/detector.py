from multiprocessing import Queue

from streamer.app_settings import AppSettings


def detector(frame_queue: Queue, detections_queue: Queue):
    app_settings = AppSettings()
