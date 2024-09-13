from multiprocessing import Queue

from detector.frame_motion_detector import MotionContoursDetector
from streamer.app_settings import AppSettings


def detector(frame_queue: Queue, detections_queue: Queue):
    app_settings = AppSettings()
    motion_contours_detector = MotionContoursDetector()

    prev_frame = frame_queue.get()
    while True:
        # Blocking function to detect a new frame in the queue
        frame = frame_queue.get()
        # None signals the video ended
        if frame is None:
            break

        motion_contours = motion_contours_detector.get_detection(prev_frame, frame)
        prev_frame = frame
