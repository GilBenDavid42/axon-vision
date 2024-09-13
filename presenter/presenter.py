from multiprocessing import Queue

from project.streamer.app_settings import AppSettings


def presenter(detections_queue: Queue):
    app_settings = AppSettings()
