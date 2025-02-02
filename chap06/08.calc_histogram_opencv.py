import numpy as np, cv2

# 영상 파일 읽기
image = cv2.imread("./images/pixel.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 히스토그램 계산
hsize, ranges = [32], [0, 256] # 히스토그램 간격수, 값 범위
hist_opencv = cv2.calcHist([image], [0], None, hsize, ranges) # OpenCV 함수

# 히스토그램 출력
print("OpenCV 함수: \n", hist_opencv.flatten()) # 행렬을 벡터로 변환하여 출력

# 원본 이미지 출력
cv2.imshow("image", image)
cv2.waitKey(0)