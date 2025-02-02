import numpy as np
import cv2
# 단일 채널 생성 및 초기화
matrix1 = np.full((3, 5), 20, np.uint8)
matrix2 = np.full((3, 5), 40, np.uint8)

# 마스크 생성
mask = np.zeros(matrix1.shape, np.uint8)
mask[:, 1:4] = 1 # 관심 영역을 지정한 후, 1을 할당

# 행렬 덧셈
add_result1 = cv2.add(matrix1, matrix2)
add_result2 = cv2.add(matrix1, matrix2, mask=mask) # 관심 영역만 덧셈 수행
# 행렬 나눗셈
div_result = cv2.divide(matrix1, matrix2)
# 결과 출력
titles = ['matrix1', 'matrix2', 'mask', 'add_result1', 'add_result2', 'div_result']
for title in titles:
    print(f"[{title}] = \n{eval(title)} \n")