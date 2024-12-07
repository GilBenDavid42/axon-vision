from multiprocessing import Queue

from presenter.present_motion import MotionPresenter


def presenter(detections_queue: Queue, video_settings_queue: Queue):
    fps = video_settings_queue.get()
    # Convert FPS to milliseconds
    fps_milliseconds = int(1000 / fps)
    motion_presenter = MotionPresenter(fps_milliseconds)

    # Start receiving frames with motion
    while True:
        # Blocking function to receive a new detection in the queue
        detection = detections_queue.get()
        # None signals the video ended
        if detection is None:
            break
        (frame, motion_contours) = detection

        motion_presenter.present(frame, motion_contours)
