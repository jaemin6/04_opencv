import cv2
import numpy as np
# 이미지 불러오기
img = cv2.imread('../img/fish.jpg')
rows, cols = img.shape[0:2]  # 영상 크기 shape는 높이 너비를 얘기함

dx, dy = 100, 50      # 이동 할 픽셀 거리

# 변환 행렬 생성
mtrx = np.float32([[1, 0, dx], [0, 1, dy]])   # x에 dx 더하고, y에 dy 더함
# 이동 행렬을 이용 이미지를 이동시킴
dst = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy))
# 테두리를 채우는 방법, BORDER_CONSTANT로 지정 (빈 부분은 (255, 0, 0) → 파란색)
dst2 = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255, 0, 0))
# cv2.INTER_LINEAR: 보간법 (픽셀 위치 이동 시 부드럽게 처리)
dst3 = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('original', img)
cv2.imshow('trans', dst)
cv2.imshow('BORDER_CONSTATNT', dst2)
cv2.imshow('BORDER_FEFLECT', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()