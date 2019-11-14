import cv2
import numpy as np
class ColorDetector:
    def __init__(self):
        pass

    def detect(self, image, strdata):

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        image = cv2.inRange(hsv, (int(strdata[1]), int(strdata[2]), int(strdata[3])),
                        (int(strdata[4]), int(strdata[5]), int(strdata[6])))

        return image
