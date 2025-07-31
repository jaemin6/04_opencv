import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')
height, width = img.shape[:2]


m_small = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
m_big = np.float32([[2, 0, 0], [0, 2, 0]])

dst_small = cv2.warpAffine(img, m_small, (int(w*0.5), int(h*0.5)))
dst_big   = cv2.warpAffine(img, m_big,   (int(w*2),   int(h*2))


# 결과 출력
cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
cv2.imshow("small INTER_AREA", dst3)
cv2.imshow("big INTER_CUBIC", dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()