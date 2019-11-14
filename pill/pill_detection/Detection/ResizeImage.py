import numpy as np
import cv2
import os
import datetime
import matplotlib.pyplot as plt


class ResizeImage:

    dt = datetime.datetime.now()
    path = "/image/" + "x5.jpg"
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = dirname + path
    # print(path)


    img = cv2.imread(path)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
    out_ ,contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    s = list()

    for cnt in contours:
        # x, y, w, h = cv2.boundingRect(cnt)
        s.append(cv2.boundingRect(cnt))

    s.sort(key=lambda x: x[2], reverse=True)
    # img = img[s[1][1]:s[1][1] + s[1][3], s[1][0]:s[1][0] + s[1][2]]
    img = img[s[1][1] - 100:s[1][1] + s[1][3] + 100, s[1][0] - 170:s[1][0] + s[1][2] + 100]
    # img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation= cv2.INTER_AREA)

    # img = cv2.pyrDown(img)
    # img = cv2.pyrDown(img)

    cv2.imshow('a', img)
    cv2.imwrite(path+"ng.jpg", img)

    cv2.waitKey()
    cv2.destroyAllWindows()

