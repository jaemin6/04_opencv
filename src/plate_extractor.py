import cv2
import numpy as np

img = cv2.imread('img/car_01.jpg')
draw = img.copy()
rows, cols = img.shape[:2]

pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

def onMouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x,y), 10, (0,255,255), -1)
        cv2.imshow("License Plate Extractor", draw)
        pts[pts_cnt] = [x,y]
        pts_cnt += 1






cv2.imshow("License Plate Extractor", img)
cv2.setMouseCallback("License Plate Extractor", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
