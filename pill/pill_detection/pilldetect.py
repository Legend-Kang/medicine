#coding=utf-8
import django
import os
import cv2
import pytesseract
import numpy as np

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pill.settings")
django.setup()

import operator

import datetime

from pill_detection.models import Photo

from pill_detection.Detection import DetectShape
from pill_detection.Detection import DetectColor
from pill_detection.Detection import PossibleChar
from pill_detection.Detection import DetectChars
from pill_detection.Detection import Search_char

from django.http import HttpResponse





# 영상 확인용
showSteps = False



def main():

    pb = Photo.objects.last()
    pd = str(pb.photo)
    print(pb.photo)



    # 쉐입 디텍터,
    sd = DetectShape.ShapeDetector()
    # 컬러 디텍터,
    dc = DetectColor.ColorDetector()
    # 글자 서치
    sc = Search_char.Search_char()

    dt = datetime.datetime.now()
    # path = "/image/"+ dt.strftime("%d") + "/q6.jpg"
    path = "/image/" + pd
    # path = "/image/" + "g2.jpg"
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(dirname)
    path = dirname + path
    # print(path)

    ######## 이미지 사이즈 조절 ########
    img = cv2.imread(path)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
    out_, contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    s = list()

    for cnt in contours:
        # x, y, w, h = cv2.boundingRect(cnt)
        s.append(cv2.boundingRect(cnt))

    s.sort(key=lambda wa: wa[2], reverse=True)
    img = img[s[1][1] - 100:s[1][1] + s[1][3] + 100, s[1][0] - 200:s[1][0] + s[1][2] + 100]
    # img = cv2.resize(img, dsize= (380, 280))
    img = cv2.resize(img, dsize=(400, 300))

    cv2.imwrite(dirname + "/image/new2.jpg", img)


    ##########################################

    ################ 색상 검출 ################
    # 11.10 오후 11:42분 수정부분
    image = cv2.imread(dirname + "/image/new2.jpg", cv2.IMREAD_ANYCOLOR)

    if showSteps :
        cv2.imshow("test1", image)
    f = open(os.path.dirname(__file__)+'/color2.txt', "r")
    text = f.readlines()
    count = len(text)
    color_a = [0, 0, 0, 0, 0]
    t = [0, 0, 0, 0, 0]

    for i in range(count):
        strdata = text[i].split(' ')
        out = dc.detect(image, strdata)
        img_, contours, _ = cv2.findContours(out, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        try:
            outer = max(contours, key=lambda x: cv2.contourArea(x))
            # print("색상순서 : "+ strdata[0])
            # print(cv2.contourArea(outer))
            if(cv2.contourArea(outer)>=23000):
                color_a[i] = [0, strdata[0], outer]
                t[i] = 0
            else:
                color_a[i] = [cv2.contourArea(outer), strdata[0], outer]
                t[i] = cv2.contourArea(outer)
        except ValueError:      # 색상이 맞지 않을 경우 생기는 넓이 오류 발생시 예외처리
            pass

    mx = t.index(max(t))
    strdata = text[mx].split(' ')
    store_color_data = strdata[0]
    out = dc.detect(image, strdata)
    black_background = out

    if (showSteps):
        cv2.imshow("COLOR", out)




    # 배경 제거
    black_background = cv2.medianBlur(black_background, 21)
    image = cv2.bitwise_and(image, image, mask=black_background)
    cv2.imwrite(dirname + "/image/new3.jpg", image)

    if showSteps :
        cv2.imshow("original", image)

    character = []
    #####################################################################
    # 글자인식을 위한 이미지 처리

    for i in range(1,6):
        if(i == 1):
            # 첫번째 방법(이미지 처리)
            print("*********첫번째 이미지 처리*********")
            img_t = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(img_t, ksize=(5,5), sigmaX=0)
            threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, 9)
            median = cv2.bitwise_not(threshold)

        # if(i == 2):
        #     # 두번째 방법(이미지 처리)
        #     print("*********두번째 이미지 처리*********")
        #     img_t = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #     threshold = cv2.adaptiveThreshold(img_t, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 3)
        #     #  이미지 이진화
        #     median = cv2.medianBlur(threshold, 3)
        #     #  노이즈 제거
        #     median = cv2.bitwise_not(median)
        #     # 비트연산을 통한 색반전

        if (i == 2):
            # 두번째 방법(이미지 처리)
            print("*********두번째 이미지 처리*********")
            img_t = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(img_t, ksize=(3, 3), sigmaX=0)
            threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 5)
            median = cv2.bitwise_not(threshold)


        if(i == 3):
            # 세번째 방법(이미지 처리)
            print("*********세번째 이미지 처리*********")
            img_t = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(img_t, ksize=(3, 3), sigmaX=0)
            threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 9)
            median = cv2.bitwise_not(threshold)

        if (i == 4):
            # 네번째 방법(이미지 처리)
            print("*********네번째 이미지 처리*********")
            img_t = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(img_t, ksize=(3, 3), sigmaX=0)
            threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, 5)
            median = cv2.bitwise_not(threshold)

        if (i == 5):
            # 다섯번째 방법(이미지 처리)
            print("*********다섯번째 이미지 처리*********")
            img_t = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(img_t, ksize=(3, 3), sigmaX=0)
            threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 9)
            median = cv2.bitwise_not(threshold)

        # if (i == 1):
        #     cv2.imshow("contours drawn1", median)
        # if (i == 2):
        #     cv2.imshow("contours drawn2", median)
        # if (i == 3):
        #     cv2.imshow("contours drawn3", median)

        #####################################################################
        # 글자인식을 위한 이미지 처리 끝


        #####################################################################
        # 글자인 부분 찾기

        img_, contours, _ = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        chars = []
        charst = []
        # print("*******************")
        # for cnt in contours:
        #     print(cv2.contourArea(cnt))
        # print("*******************")
        for cnt in contours:
            if 12 < cv2.contourArea(cnt) and cv2.contourArea(cnt) < 800:
                charst.append(cnt)
            if 10 < cv2.contourArea(cnt) and cv2.contourArea(cnt) < 800:
                # print(cv2.contourArea(cnt))
                chars.append(cnt)
        listOfPossibleChars = []
        intCountOfPossibleChars = 0
        output = np.zeros((img_t.shape[0], img_t.shape[1], 3), np.uint8)
        output1 = np.zeros((img_t.shape[0], img_t.shape[1], 3), np.uint8)


        for m in range(0, len(charst)):
            cv2.drawContours(output1, charst[m], -1, (255, 255, 255), 3)

        chartt = pytesseract.image_to_string(output1, lang='eng',
                                             config='--tessdata-dir "C://projects//Tesseract-OCR//tessdata" --psm 7 --oem 1')
        character.append(chartt)
        # if (i == 2):
        #     cv2.imshow("test22", output1)
        #     print("chartt22 : " + chartt)
        # if(i==3):
        #     cv2.imshow("test33", output1)
        #     print("chartt33 : " + chartt)

        # print("*********2**********")
        for k in range(0, len(chars)):                       # for each contour
            possibleChar = PossibleChar.PossibleChar(chars[k])
            # print(chars[i])
            cv2.drawContours(output, chars[k], -1, (255,255,255),2)
            # if (i == 1):
            #     cv2.imshow("char1_1", output)
            # if (i == 2):
            #     cv2.imshow("char1_2", output)
            # if (i == 3):
            #     cv2.imshow("char1_3", output)

            if DetectChars.checkIfPossibleChar(possibleChar):
                intCountOfPossibleChars = intCountOfPossibleChars + 1
                listOfPossibleChars.append(possibleChar)
        # print("*********2**********")

        chars2 = pytesseract.image_to_string(output, lang='eng',
                                             config='--tessdata-dir "C://projects//Tesseract-OCR//tessdata" --psm 7 --oem 1')
        character.append(chars2)

        # print("char1_%d : " %i + chars2)
        out = []
        for possibleChar in listOfPossibleChars:
            out.append(possibleChar.contour)


        output = np.zeros((img_t.shape[0], img_t.shape[1], 3), np.uint8)
        kernel = np.ones((3, 3), np.uint8)

        cv2.drawContours(output, out, -1, (255,255,255), 2)
        # if (i == 1):
        #     cv2.imshow("char2_1", output)
        # if (i == 2):
        #     cv2.imshow("char2_2", output)
        # if (i == 3):
        #     cv2.imshow("char2_3", output)
        # ret2, output = cv2.threshold(output, 127, 255, cv2.THRESH_BINARY_INV)
        # output = cv2.morphologyEx(output, cv2.MORPH_ERODE, kernel, dst=None, anchor=(-1, -1), iterations=1)
        output = cv2.morphologyEx(output, cv2.MORPH_CLOSE, kernel, iterations=1)

        # if (i == 1):
        #     cv2.imshow("char3_1", output)
        # # if (i == 2):
        # #     cv2.imshow("char3_2", output)
        # if (i == 3):
        #     cv2.imshow("char3_3", output)

        # if showSteps :
        #     cv2.imshow("output", output)
        # opened = cv2.morphologyEx(output, cv2.MORPH_ERODE, kernel, dst=None, anchor=(-1, -1), iterations=1)
        # if showSteps :
        #     cv2.imshow("output", opened)


        chars = pytesseract.image_to_string(output, lang='eng', config= '--tessdata-dir "C://projects//Tesseract-OCR//tessdata" --psm 7 --oem 1')
        character.append(chars)

        # print("char3_%d : " %i + chars)
        # print(chars2)
        # 쉐입 디텍션입니다.
        # outer = max(contours, key=lambda x: cv2.contourArea(x))
        shape = sd.detect(outer)
        # shape = sd.detect(color_a[mx][2])

    print("shape : " + shape)
    print("color : " + store_color_data)
    print(character)
    csh = sc.searh_c(store_color_data, character)
    print(csh)
    chars = csh

    # cv2.waitKey(0)
    # print("")

    return(shape, chars, store_color_data)

if __name__ == '__main__':
    main()

