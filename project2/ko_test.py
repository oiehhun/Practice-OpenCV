from PIL import Image
import numpy as np
import pytesseract

filename = './images/sample.png'
config = ('-l kor+eng')
# config = ('-l kor+eng --oem 3 --psm 11') # oem, psm은 OCR 엔진 모드와 페이지 세분화 모드에 대해 세팅
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1, config=config)
print(text)