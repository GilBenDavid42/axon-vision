from multiprocessing import Process, Queue

from detector import detector
from presenter import presenter
from streamer import streamer


def main():
    """
    Manages all processes of streamer, detector and presenter
    letting them send messages to each other trough multiprocessing.Queue
    """

    # A queue for a general video settings passed from streamer to presenter
    video_settings_queue = Queue()

    # A queue for a frames passed from streamer to detector
    frame_queue = Queue()
    streamer_process = Process(target=streamer, args=(frame_queue, video_settings_queue))

    # A queue for detections passed from detector to presenter
    detections_queue = Queue()

    detector_process = Process(target=detector, args=(frame_queue, detections_queue))
    presenter_process = Process(target=presenter, args=(detections_queue, video_settings_queue))

    streamer_process.start()
    detector_process.start()
    presenter_process.start()

    streamer_process.join()
    detector_process.join()
    presenter_process.join()


if __name__ == '__main__':
    main()
