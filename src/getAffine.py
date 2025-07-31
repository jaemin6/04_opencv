import cv2
import numpy as np
from matplotlib import pyplot as plt

# 이미지 불러오기
file_name = '.../img/fish.jpg'
img = cv2.imread(file_name)
rows, cols = img.shape[:2]


# 어핀 변환 적용
dst = cv2.warpAfine(img, mtrx, (int(cols * 1.5), rows))

# 결과 출력
cv2.imshow('origin', img)
cv2.imshow('affin', dst)
cv2.waitKey()
cv2.destroyAllWindows()