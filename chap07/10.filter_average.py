import numpy as np, cv2

image = cv2.imread("./images/filter_avg.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

blur_img = cv2.blur(image, (5, 5), borderType=cv2.BORDER_DEFAULT) # OpenCV의 블러링 함수
box_img = cv2.boxFilter(image, ddepth=-1, ksize=(5, 5)) # OpenCV의 박스 필터 함수  

cv2.imshow("image", image),
cv2.imshow("blur_img", blur_img)
cv2.imshow("box_img", box_img)
cv2.waitKey(0)