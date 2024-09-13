import cv2


class MotionPresenter:
    def __init__(self, fps_milliseconds):
        self.fps_milliseconds = fps_milliseconds

    def present(self, frame, motion_contours):
        # Draw bounding boxes around detected motion
        for contour in motion_contours:
            if cv2.contourArea(contour) < 500:  # Ignore small movements
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with motion detection
        cv2.imshow("Motion Detection", frame)

        cv2.waitKey(self.fps_milliseconds)
