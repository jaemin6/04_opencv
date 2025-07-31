import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('../img/fish.jpg')

# 이동 거리
dx, dy = 100, 50

# 변환 행렬
mtrx = np.float32([[1, 0, dx], [0, 1, dy]])

# 이동 적용 (출력 이미지 크기 조정 필요)
dst = cv2.warpAffine(img, mtrx, (img.shape[1] + dx, img.shape[0] + dy))

# 결과 출력
cv2.imshow('original', img)
cv2.imshow('translated', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
