import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')
height, width = img.shape[:2]
# 크기 지정으로 축소 (절대 크기 입력)
dst1 = cv2.resize(img, (int(width*0.5), int(height*0.5)), \
                         interpolation=cv2.INTER_AREA)
# 높이와 너비를 각각 50%로 줄임, INTER_AREA: 축소 시 적합한 보간법

# 배율 지정으로 확대 (상대 배율 입력)
dst2 = cv2.resize(img, None,  None, 2, 2, cv2.INTER_CUBIC)
# 가로, 세로 모두 2배 확대 / INTER_CUBIC: 확대 시 선명하게

# 결과 출력
cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resize가 훨씬 간편하고 직관적, 원하는 픽셀 크기 바로 지정가능, fx, fy만 지정하면 자동으로 확대 축소