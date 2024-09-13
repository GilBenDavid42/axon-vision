from multiprocessing import Queue

from project.streamer.app_settings import AppSettings


def streamer(frame_queue: Queue):
    app_settings = AppSettings()
