import numpy as np
import cv2

# 색상 선언
orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black, green, magenta = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 255)

# 컬러 영상 생성 및 초기화: 크기 (400, 600)
image = np.full((400, 600, 3), white, np.uint8)

# 새로운 동그라미 위치 좌표
center = (300, 200) # 영상의 중심 좌표
pt1, pt2 = (200, 100), (450, 300)
shade = (pt2[0] + 2, pt2[1] + 2) # 그림자 좌표

# 원 그리기
cv2.circle(image, center, 100, blue) # 중심에 큰 원
cv2.circle(image, pt1, 50, orange, 2) # 좌측 상단에 작은 원
cv2.circle(image, pt2, 70, cyan, -1) # 우측 하단에 채워진 큰 원

# 텍스트 출력
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, "Hello World", (200, 200), font, 1.0, green, 2)
cv2.putText(image, "OpenCV Rocks", (400, 100), font, 0.8, magenta, 2)
cv2.putText(image, "Circle Cyan", shade, font, 1.2, black, 2) # 그림자 효과
cv2.putText(image, "Circle Cyan", pt2, font, 1.2, cyan, 1)

# 윈도우에 영상 표시
title = "Draw Circles"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0) # 아무키나 누르면
cv2.destroyAllWindows() # 모든 열린 윈도우 닫기