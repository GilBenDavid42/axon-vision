from typing import Tuple

import cv2
from numpy import ndarray


class MotionPresenter:
    def __init__(self, fps_milliseconds):
        self.fps_milliseconds = fps_milliseconds

    def present(self, frame: ndarray, motion_contours: Tuple[ndarray]):
        # Draw bounding boxes around detected motion
        for contour in motion_contours:
            if cv2.contourArea(contour) < 500:  # Ignore small movements
                continue
            (x, y, w, h) = cv2.boundingRect(contour)

            rectangle = frame[y:y + h, x:x + w]

            # Apply Gaussian blur to the ROI
            blurred_rectangle = cv2.GaussianBlur(rectangle, (21, 21), 0)

            # Replace the original ROI with the blurred one
            frame[y:y + h, x:x + w] = blurred_rectangle

        # Display the frame with motion detection
        cv2.imshow("Motion Detection", frame)

        cv2.waitKey(self.fps_milliseconds)
