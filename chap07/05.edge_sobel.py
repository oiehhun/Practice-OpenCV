import numpy as np, cv2

image = cv2.imread("./images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
    
#  OpenCV 제공 소벨 에지 계산
# x방향 미분 - 수직 마슽크, ksize는 커널의 크기
dst1 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, ksize=3)
# y방향 미분 - tnwjd 마스크
dst2 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, ksize=3)

dst1 = cv2.convertScaleAbs(dst1)
dst2 = cv2.convertScaleAbs(dst2)

cv2.imshow("edge- sobel edge", image)
cv2.imshow("dst1- vertical_OpenCV", dst1)
cv2.imshow("dst2- horizontal_OpenCV", dst2)
cv2.waitKey(0)