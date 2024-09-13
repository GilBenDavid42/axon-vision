from multiprocessing import Queue

from detector.motion_contours import get_motion_contours


def detector(frame_queue: Queue, detections_queue: Queue):
    prev_frame = frame_queue.get()
    while True:
        # Blocking function to detect a new frame in the queue
        frame = frame_queue.get()
        # None signals the video ended
        if frame is None:
            break

        motion_contours = get_motion_contours(prev_frame, frame)
        detections_queue.put((frame, motion_contours))
        prev_frame = frame

    detections_queue.put(None)
