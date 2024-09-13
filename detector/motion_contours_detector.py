from pathlib import Path

import cv2
import imutils


class MotionContoursDetector:
    def __init__(self, video_path: Path):
        self.video_path = video_path

    def get_detection(self, prev_frame, frame):
        # Convert frames to grayscale
        perv_gray_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Compute the absolute difference between current and previous frame
        diff = cv2.absdiff(gray_frame, perv_gray_frame)

        # Apply threshold to get the binary image representing the motion areas
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours of the motion areas
        motion_contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        yield imutils.grab_contours(motion_contours)
