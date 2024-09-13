from multiprocessing import Process, Queue

from detector import detector
from presenter import presenter
from streamer import streamer


def main():
    video_settings_queue = Queue()
    frame_queue = Queue()
    streamer_process = Process(target=streamer, args=(frame_queue, video_settings_queue))
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
