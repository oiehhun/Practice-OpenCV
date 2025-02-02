import cv2
image = cv2.imread("./images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 에러")

# 새로운 JPEG 화질 설정 및 PNG 압축 레벨 설정
params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 50) # JPEG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 5] # PNG 압축 레벨 설정

# 행렬을 영상파일로 저장
cv2.imwrite("./output_images/high_quality.jpg", image) # 디폴트는 95
cv2.imwrite("./output_images/medium_quality.jpg", image, params_jpg) # 지정 화질로 저장
cv2.imwrite("./output_images/medium_compression.png", image, params_png)
cv2.imwrite("./output_images/image_output.bmp", image) # BMP 파일로 저장

print("저장 완료")