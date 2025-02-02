#  PC 카메라를 통해 받아온 프레임에 다음의 영상처리를 수행하고, 결과 영상을 윈도우에 표시하는 프로그램을 작성하시오

## (200, 100)좌표에서 100X200 크기의 관심 영역 지정
## 관심 영역에서 녹색 성분을 50만큼 증가
##  관심 영역의 테두리를 두께 3의 빨간색으로 표시

import cv2
capture = cv2.VideoCapture(0) # 0번 카메라 연결

if capture.isOpened() == False: raise Exception("카메라 연결 안됨")
fps = 30 # 초당 프레임 수
delay = round(1000/ fps) # 프레임 간 지연 시간
size = (640, 480) # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 압축 코덱 설정

while True: # 무한 반복
    ret, frame = capture.read() # 카메라 영상 받기
    if not ret: break
    x, y, w, h = (200,100, 100,200)
    cv2.rectangle(frame, (x,y,w,h) , (0,0,255), 3 )
    blue, green, red = cv2.split(frame)
    tmp = green[y:y+h, x:x+w]
    cv2.add(tmp, 50, tmp)
    frame = cv2.merge([blue, green, red])
    if cv2.waitKey(delay) >= 0: break
    cv2.imshow("ex16", frame) # 윈도우에 영상 띄우기
capture.release()


