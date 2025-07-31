import cv2
import numpy as np
import datetime
import os

img = cv2.imread('../img/car_01.jpg')
draw = img.copy()
rows, cols = img.shape[:2]

pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

def onMouse(event, x, y, flags, param):
    global pts_cnt, pts
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x,y), 10, (0,255,255), -1)
        cv2.imshow("License Plate Extractor", draw)
        pts[pts_cnt] = [x,y]
        pts_cnt += 1

        if pts_cnt == 4:
            pts1 = np.array(pts, dtype=np.float32)
            
            sm = pts.sum(axis=1)                
            diff = np.diff(pts, axis=1) 

            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]

            pts1 = np.array([topLeft, topRight, bottomRight, bottomLeft], dtype=np.float32)

            width, height = 300, 150
            pts2 = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (width, height))

            now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_dir = r'C:\Users\405\project\opencv_tutorial\04_opencv\extracted_plates'
            filename = f"plate_{now}.png"
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, result)

            pts_cnt = 0
            pts = np.zeros((4, 2), dtype=np.float32)
            draw[:] = img.copy()
            cv2.imshow("License Plate Extractor", draw)

 

    






cv2.imshow("License Plate Extractor", img)
cv2.setMouseCallback("License Plate Extractor", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
