from multiprocessing import Queue

from presenter.present_motion import present_motion


def presenter(detections_queue: Queue):
    while True:
        # Blocking function to detect a new frame in the queue
        detection = detections_queue.get()
        # None signals the video ended
        if detection is None:
            break
        (frame, motion_contours) = detection

        present_motion(frame, motion_contours)
