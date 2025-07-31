import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')
rows, cols = img.shape[:2]

angle = 45 * np.pi / 180  # 회전 각도 
m = np.float32([[np.cos(angle), -np.sin(angle), tx],
                [np.sin(angle),  np.cos(angle), ty]])

rotated = cv2.warpAffine(img, m, (cols, rows))

cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()