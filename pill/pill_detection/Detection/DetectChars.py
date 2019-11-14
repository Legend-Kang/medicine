# DetectChars.py
import os

import cv2
import numpy as np
import math
import random

# import Main
# import Preprocess
# import PossibleChar

# module level variables ##########################################################################

kNearest = cv2.ml.KNearest_create()

        # constants for checkIfPossibleChar, this checks one possible char only (does not compare to another char)
MIN_PIXEL_WIDTH = 5
MIN_PIXEL_HEIGHT = 9

MIN_ASPECT_RATIO = 0.12
# 0.25
MAX_ASPECT_RATIO = 4
# 1.15
MIN_PIXEL_AREA = 100
MAX_PIXEL_AREA = 2600

def checkIfPossibleChar(possibleChar):
    # print(" -------- ")
    # print("MIN_Area", possibleChar.intBoundingRectArea  , " > " ,MIN_PIXEL_AREA)
    # print("WIDTH ", possibleChar.intBoundingRectWidth ," > " ,MIN_PIXEL_WIDTH )
    # print("HEIGHT ", possibleChar.intBoundingRectHeight ," > " ,MIN_PIXEL_HEIGHT)
    # print("MIN_ASPECT_RATIO ", possibleChar.fltAspectRatio," > ",MIN_ASPECT_RATIO)
    # print("MAX_ASPECT_RATIO ", possibleChar.fltAspectRatio," < " ,MAX_ASPECT_RATIO)
    # print("MAX_PIXEL_AREA ", possibleChar.intBoundingRectArea ," < " ,MAX_PIXEL_AREA)

    if (possibleChar.intBoundingRectArea > MIN_PIXEL_AREA and
        possibleChar.intBoundingRectWidth > MIN_PIXEL_WIDTH and
            possibleChar.intBoundingRectHeight > MIN_PIXEL_HEIGHT and
        MIN_ASPECT_RATIO < possibleChar.fltAspectRatio and
            possibleChar.fltAspectRatio < MAX_ASPECT_RATIO and
            possibleChar.intBoundingRectArea < MAX_PIXEL_AREA):
        # print("True")
        # print(" -------- ")
        return True
    else:
        # print(" -------- ")
        # print("MIN_Area", possibleChar.intBoundingRectArea, " > ", MIN_PIXEL_AREA)
        # print("WIDTH ", possibleChar.intBoundingRectWidth, " > ", MIN_PIXEL_WIDTH)
        # print("HEIGHT ", possibleChar.intBoundingRectHeight, " > ", MIN_PIXEL_HEIGHT)
        # print("MIN_ASPECT_RATIO ", possibleChar.fltAspectRatio, " > ", MIN_ASPECT_RATIO)
        # print("MAX_ASPECT_RATIO ", possibleChar.fltAspectRatio, " < ", MAX_ASPECT_RATIO)
        # print("MAX_PIXEL_AREA ", possibleChar.intBoundingRectArea, " < ", MAX_PIXEL_AREA)
        # print("False")
        # print(" -------- ")
        return False
