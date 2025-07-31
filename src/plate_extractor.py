import cv2
import numpy as np
import datetime
import os

image_files = [f"../img/car_0{i}.jpg" for i in range(1, 8)]  # 이미지를 갖고있는 번호만큼 반복문 사용
current_img_index = 0

img = cv2.imread(image_files[current_img_index])
draw = img.copy()   # draw 변수에 img 복사해서 저장
rows, cols = img.shape[:2]

pts_cnt = 0    # 클릭한 좌표 갯수 카운ㅌ
pts = np.zeros((4,2), dtype=np.float32)  #pts는 4개의 좌표를 저장하는 2차원 배열, 각 좌표는 (x,y)형태이며 float32 타입

# 저장되는 경로
output_dir = r'C:\Users\405\project\opencv_tutorial\04_opencv\extracted_plates'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# 마우스 이벤트 사용 함수 
def onMouse(event, x, y, flags, param):   # x, y는 마우스 커서 좌표
    global pts_cnt, pts, current_img_index, img, draw, rows, cols
     # 마우스 이벤트 발생 했을 때만 실행
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x,y), 10, (0,255,255), -1)    # 반지름 크기 설정 노란색 원 설정
        cv2.imshow("License Plate Extractor", draw)     # 실시간 클릭 위치 표시
        pts[pts_cnt] = [x,y]
        pts_cnt += 1                             # 클릭한 좌표 저장, 다음 좌표 저장 준비

        if pts_cnt == 4:                         # 좌표 4개 선택 후 원근 변환 실행 준비
            sm = pts.sum(axis=1)                
            diff = np.diff(pts, axis=1) 

            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]
            # 순서 좌상단 우 상단, 우 하단 좌 하단 순
            pts1 = np.array([topLeft, topRight, bottomRight, bottomLeft], dtype=np.float32)

            width, height = 300, 150   # 변환 후 이미지 지정
            pts2 = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (width, height))

            now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')  # 타임스탬탬 역할, 저장 된 이름
            filename = f"plate_{now}.png"
            filepath = os.path.join(output_dir, filename)   # 저장 폴더 경로, 파일명 png 전환

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
                cv2.destroyAllWindows()   # 초기 상태 마우스 대기
                return

            img = cv2.imread(image_files[current_img_index])
            draw = img.copy()
            rows, cols = img.shape[:2]
            cv2.imshow("License Plate Extractor", draw)

cv2.imshow("License Plate Extractor", img)
cv2.setMouseCallback("License Plate Extractor", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
