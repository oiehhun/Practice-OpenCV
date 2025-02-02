import cv2
import numpy as np
import random

# 원 생성 및 동영상 저장
video_filename = "cirdect.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20
frame_size = (640, 480)

# 사용자 입력: 생성할 원 개수
num_circles = int(input("생성할 원 개수를 입력하세요: "))

out = cv2.VideoWriter(video_filename, fourcc, fps, frame_size)

# 원을 랜덤으로 생성하여 프레임에 추가
def create_frame(num_circles):
    img = np.zeros((480, 640, 3), np.uint8)
    img[:] = (255, 255, 255)  # 흰색 배경

    for _ in range(num_circles):  # 입력된 개수만큼 원 생성
        x = random.randint(50, 590)
        y = random.randint(50, 430)
        radius = random.randint(20, 50)
        color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Blue, Green, Red
        cv2.circle(img, (x, y), radius, color, -1, cv2.LINE_AA)

    return img

# 동영상 생성
for _ in range(fps * 5):  # 5초 길이의 동영상 생성
    frame = create_frame(num_circles)
    out.write(frame)

out.release()
print(f"영상이 저장되었습니다: {video_filename}")

# 영상 파일 읽기
capture = cv2.VideoCapture(video_filename)
if not capture.isOpened():
    print("영상을 열 수 없습니다.")
    exit()

# 색상 이름 변환 함수
def get_color_name(color):
    b, g, r = color
    if r > g and r > b:
        return "Red"
    elif g > r and g > b:
        return "Green"
    elif b > r and b > g:
        return "Blue"
    else:
        return "Unknown"

# 원 탐지 및 처리 함수
def detect_and_annotate(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)  # 블러링으로 노이즈 제거

    # 원 탐지
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=20, maxRadius=100
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))  # 원 좌표와 반지름 반올림
        for (x, y, r) in circles[0, :]:
            # 원 내부 색상 가져오기 (중앙 픽셀)
            color = frame[y, x]
            color_name = get_color_name(color)

            # 바운딩 박스 그리기
            cv2.rectangle(frame, (x - r, y - r), (x + r, y + r), (0, 255, 255), 2)

            # 텍스트 출력
            cv2.putText(frame, color_name, (x - r, y - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return frame

# 비디오 처리 및 출력
while True:
    ret, frame = capture.read()
    if not ret:
        break

    # 원 탐지 및 주석 추가
    annotated_frame = detect_and_annotate(frame)

    # 결과 영상 출력
    cv2.imshow("Detected Circles", annotated_frame)

cv2.waitKey(0)
capture.release()
cv2.destroyAllWindows()