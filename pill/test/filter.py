#-*- coding: utf-8 -*-
import cv2
import sys
import numpy as np

def nothing(x):
    pass

# Load in image

image = cv2.imread('q3.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a window
cv2.namedWindow('image')

# create trackbars for change
cv2.createTrackbar('Ksize','image',0,9,nothing)
cv2.createTrackbar('Threshold_blocksize','image',1,25,nothing)
cv2.createTrackbar('Threshold_c','image',1,16,nothing)
# cv2.createTrackbar('VMin','image',0,255,nothing)


# Set default value for MAX trackbars.
cv2.setTrackbarPos('Ksize', 'image', 5)
cv2.setTrackbarPos('Threshold_blocksize', 'image', 10)
cv2.setTrackbarPos('Threshold_c', 'image', 2)

# Initialize to check if HSV min/max value changes
# ksize, threshold_blocksize, threshold_c = 0
# pksize, pthreshold_blocksize, pthreshold_c = 0
ksize =0
pksize =0


output = image
wait_time = 33

while(1):

    # get current positions of all trackbars
    ksize = cv2.getTrackbarPos('Ksize','image')
    ksize = ksize*2 +1
    threshold_blocksize = cv2.getTrackbarPos('Threshold_blocksize','image')
    threshold_blocksize= threshold_blocksize*2 + 1
    threshold_c = cv2.getTrackbarPos('Threshold_c','image')
    threshold_c = threshold_c*2 + 1


    # Create HSV Image and threshold into a range.
    blurred = cv2.GaussianBlur(image, (ksize, ksize), sigmaX=0)
    threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, threshold_blocksize, threshold_c)
    output = cv2.bitwise_not(threshold)


    # Print if there is a change in HSV value
    if(ksize != pksize):
        print("(Ksize = %d, Threshold_blocksize = %d, Threshold_c = %d)" % (ksize, threshold_blocksize, threshold_c))
        pksize = ksize

    # if( (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
    #     print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
    #     phMin = hMin
    #     psMin = sMin
    #     pvMin = vMin
    #     phMax = hMax
    #     psMax = sMax
    #     pvMax = vMax

    # Display output image
    cv2.imshow('image',output)

    # Wait longer to prevent freeze for videos.
    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

