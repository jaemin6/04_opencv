import cv2
import numpy as np
import datetime
import os

# 이미지 파일 목록
image_files = [f"../img/car_0{i}.jpg" for i in range(1, 8)]
current_img_index = 0

# 이미지 불러오기
img = cv2.imread(image_files[current_img_index])
draw = img.copy()
rows, cols = img.shape[:2]

# 좌표 저장용
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)

# 결과 저장 폴더
output_dir = r'C:\Users\405\project\opencv_tutorial\04_opencv\extracted_plates'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global pts_cnt, pts, current_img_index, img, draw, rows, cols

    if event == cv2.EVENT_LBUTTONDOWN:
        # 클릭한 위치에 노란 점 찍기
        cv2.circle(draw, (x, y), 3, (0, 255, 255), -1)
        cv2.imshow("License Plate Extractor", draw)

        pts[pts_cnt] = [x, y]
        pts_cnt += 1

        if pts_cnt == 4:
            # 4개 점 정렬
            sm = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)

            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]

            pts1 = np.array([topLeft, topRight, bottomRight, bottomLeft], dtype=np.float32)

            width, height = 300, 150
            pts2 = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

            # 원근 변환
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (width, height))

            ##  그레이스케일 변환 (OCR용 흑백 이미지)
            result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

            ##  가우시안 블러 적용 (번호판 추출 후)
            result_blurred = cv2.GaussianBlur(result_gray, (5, 5), 0)  # 커널 사이즈 5x5, 표준편차 자동

            thresh_adaptive = cv2.adaptiveThreshold(result_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 11, 2)
            contours, _ = cv2.findContours(thresh_adaptive, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contour_result = cv2.cvtColor(result_gray, cv2.COLOR_GRAY2BGR)
            cv2.drawContours(contour_result, contours, -1, (0,255,0), 2)
            cv2.imshow('Contours on Plate', contour_result)
            # 파일 이름 생성
            now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"plate_{now}.png"
            filepath = os.path.join(output_dir, filename)

            # 저장
            success = cv2.imwrite(filepath, result_blurred)

            if success:
                print(f"번호판 저장 완료: {filename}")
                cv2.imshow('Extracted Plate', result_blurred)
            else:
                print("저장 실패!")

            # 초기화 및 다음 이미지로
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

# 윈도우 띄우고 콜백 등록
cv2.imshow("License Plate Extractor", img)
cv2.setMouseCallback("License Plate Extractor", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
