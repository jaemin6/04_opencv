import cv2
import numpy as np
import datetime
import os

image_files = [f"../img/car_0{i}.jpg" for i in range(1, 8)]
current_img_index = 0

img = cv2.imread(image_files[current_img_index])
draw = img.copy()
rows, cols = img.shape[:2]

pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

output_dir = r'C:\Users\405\project\opencv_tutorial\04_opencv\extracted_plates'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def onMouse(event, x, y, flags, param):
    global pts_cnt, pts, current_img_index, img, draw, rows, cols

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x,y), 10, (0,255,255), -1)
        cv2.imshow("License Plate Extractor", draw)
        pts[pts_cnt] = [x,y]
        pts_cnt += 1

        if pts_cnt == 4:
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
            filename = f"plate_{now}.png"
            filepath = os.path.join(output_dir, filename)

            success = cv2.imwrite(filepath, result)

            if success:
                print(f"번호판 저장 완료: {filename}")
                cv2.imshow('Extracted Plate', result)
            else:
                print("저장 실패!")

            # 초기화 및 다음 이미지 로드
            pts_cnt = 0
            pts = np.zeros((4, 2), dtype=np.float32)

            current_img_index += 1
            if current_img_index >= len(image_files):
                print("이미지 처리 완료")
                cv2.destroyAllWindows()
                return

            img = cv2.imread(image_files[current_img_index])
            draw = img.copy()
            rows, cols = img.shape[:2]
            cv2.imshow("License Plate Extractor", draw)

cv2.imshow("License Plate Extractor", img)
cv2.setMouseCallback("License Plate Extractor", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
