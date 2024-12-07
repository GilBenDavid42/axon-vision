from typing import Tuple

import cv2
import imutils
from numpy import ndarray


def get_motion_contours(prev_frame: ndarray, frame: ndarray) -> Tuple[ndarray]:
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
    return imutils.grab_contours(motion_contours)
