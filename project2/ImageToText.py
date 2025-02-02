import cv2
import numpy as np
import pytesseract

TESSERACT_PATH = "/opt/homebrew/Cellar/tesseract/5.5.0/bin/tesseract"
imgpath='./images/3.jpg'
win_name = "Image To Text"
img = cv2.imread(imgpath)
draw = img.copy()
pts_cnt=0
pts=np.zeros((4, 2), dtype=np.float32)


def onMouse(event, x, y, flags, param):
    global pts_cnt
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x,y]
        pts_cnt += 1
        if pts_cnt == 4:
            sm = pts.sum(axis=1)
            diff= np.diff(pts, axis=1)

            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]

            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            w1 = abs(bottomRight[0] - bottomLeft[0])
            w2 = abs(topRight[0] - topLeft[0])
            h1 = abs(topRight[1] - bottomRight[1])
            h2 = abs(topLeft[1]-bottomLeft[1])
            width = max([w1, w2])
            height = max([h1, h2])

            pts2 = np.float32([[0,0], [width-1, 0], [width-1, height-1], [0, height-1]])

            mtrx=cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (int(width), int(height)))
            cv2.imshow('scanned', result)
            img=result


def ImgProcessing():
    global img
    
    #이미지파일 그레이스케일로 변환
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #이미지파일 음영 평준화
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

    #이미지파일 가우시안블러 처리
    img=cv2.GaussianBlur(img, (3,3), 0)

    #이미지파일 오츠쓰래쉬홀드로 이산화 처리
    _, img=cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #처리된 이미지 출력
    cv2.imshow("testing", img)

    #png파일로 저장
    cv2.waitKey(0)
    cv2.imwrite('./images/processing.png', img)

    return img


def GetOCR():
    global img

    #OCR모델 불러오기
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    #OCR모델로 글자 추출
    text = pytesseract.image_to_string(img, lang='-l kor+eng')
        
    return text

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)

ImgProcessing()
cv2.waitKey(0)

text = GetOCR()
print(text)