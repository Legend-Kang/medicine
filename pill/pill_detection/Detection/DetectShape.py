import cv2

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, contour):
        shape = "Not Detected"
        eplison = cv2.arcLength(contour, closed=True)
        approx = cv2.approxPolyDP(contour, 0.04*eplison, True,None )
        cv2.drawContours(contour, [approx], 0, (0), 5)

        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            shape = "square" if aspect_ratio >=0.9 and aspect_ratio <= 1.1 else "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"

        shape = "circle"

        return shape