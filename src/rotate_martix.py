import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')
rows,cols = img.shape[0:2]  # 이미지 높이와 너비를 가져옴

# 라디안 각도 계산(60진법을 호도법으로 변경)
d45 = 45.0 * np.pi / 180    # 45도를 라디안(호도법)으로 변환
d90 = 90.0 * np.pi / 180    # 90도          ``

# 회전을 위한 변환 행렬 생성
# 45도 회전 행렬 (중심은 대략 이미지 중간쯤으로 설정)
m45 = np.float32( [[ np.cos(d45), -1* np.sin(d45), rows//2],     # 회전 공식 중 x축 방향
                    [np.sin(d45), np.cos(d45), -1*cols//4]])     # 회전 공식 중 y축 방향
m90 = np.float32( [[ np.cos(d90), -1* np.sin(d90), rows],        # 90도면 cos=0, sin=1 → 세로축 이동
                    [np.sin(d90), np.cos(d90), 0]])              # 그대로 오른쪽으로 회전

# 회전 변환 행렬 적용
r45 = cv2.warpAffine(img,m45,(cols,rows))      # 45도 회전 이미지 생성
r90 = cv2.warpAffine(img,m90,(rows,cols))      # 90도 회전 이미지 생성 (가로/세로 바뀜)

# 결과 출력
cv2.imshow("origin", img)
cv2.imshow("45", r45)
cv2.imshow("90", r90)
cv2.waitKey(0)
cv2.destroyAllWindows()