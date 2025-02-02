import numpy as np
import cv2

green, red, yellow = (0, 255, 0),(0, 0, 255),(0, 255, 255)
white = (255, 255, 255)

# 3채널 컬러 영상 생성 및 초기화: 크기 (400, 800)
image = np.full((400, 800, 3), white, np.uint8)

pt1, pt2 = (200, 200), (600, 200) # 타원 중심점
size = (150, 80) # 타원 크기 - 반지름 값임

# 타원의 중심점(2화소 원) 표시
cv2.circle(image, pt1, 1, 0, 2)
cv2.circle(image, pt2, 1, 0, 2)

# 타원 그리기
cv2.ellipse(image, pt1, size, 0, 0, 360, green, 2)
cv2.ellipse(image, pt2, size, 45, 0, 360, green, 2)

# 호 그리기
cv2.ellipse(image, pt1, size, 0, 30, 270, red, 4)
cv2.ellipse(image, pt2, size, 45, -45, 90, yellow, 4)

# 윈도우에 영상 표시
cv2.imshow("Draw Ellipse & Arc", image)
cv2.waitKey(0) # 키입력 대기
cv2.destroyAllWindows() # 모든 열린 윈도우 닫기 