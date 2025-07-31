# 번호판 이미지 처리 실습 및 교육 내용 정리 (2025-07-31)

## ✅ 1. 개요
번호판 인식을 위한 이미지 처리 과정 학습.
OpenCV를 활용해 번호판 이미지에서 다음을 실습함:
### 1. 그레이스케일 변환
### 2. 다양한 블러링 (Gaussian, Median, Bilateral)
### 3. 모폴로지 연산 (침식, 팽창, 열기, 닫기)
### 4. Adaptive Threshold 이진화
### 5. 컨투어 추출 및 시각화
### 6. 결과 이미지 저장

## ✅ 2. 사용된 주요 라이브러리
```
import cv2
import numpy as np
import os
import datetime
```

## ✅ 3. 주요 처리 흐름 정리
### 🔹 번호판 이미지 불러오기 및 그레이스케일 변환
```
img = cv2.imread('../img/plate_01.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
### 🔹 다양한 블러링 기법 적용
```
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)        # 가우시안 블러
median   = cv2.medianBlur(gray, 5)                  # 미디언 블러
bilateral= cv2.bilateralFilter(gray, 9, 75, 75)      # 바이레터럴 필터
```
#### 🔸 블러링 효과 비교
| 종류        | 목적          | 특징                   |
| --------- | ----------- | -------------------- |
| Gaussian  | 노이즈 제거      | 주변 픽셀에 가중치 적용        |
| Median    | 염료성 노이즈 제거  | 중앙값 필터               |
| Bilateral | 경계 유지하며 블러링 | 가장 느리지만 경계 보존 효과 뛰어남 |


## ✅ 4. 모폴로지 연산 (Morphological Operations)
### 🔹 사용한 커널 정의
```
k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
```
### 🔹 열기 연산 (Opening) – 노이즈 제거
```
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, k)
```
### 🔹 닫기 연산 (Closing) – 구멍 채우기
```
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, k)
```
#### 
| 연산 종류        | 순서      | 효과       |
| ------------ | ------- | -------- |
| 침식(Erosion)  | 줄어듦     | 잡음 제거    |
| 팽창(Dilation) | 커짐      | 구멍 채우기   |
| 열기(Opening)  | 침식 → 팽창 | 작은 잡음 제거 |
| 닫기(Closing)  | 팽창 → 침식 | 작은 구멍 제거 |

## ✅ 5. Adaptive Threshold (적응형 이진화)
```
thresh_adaptive = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
)
```
### 🔹 주변 픽셀 밝기 기준으로 문자를 강조하여 이진화

## ✅ 6. 컨투어(윤곽선) 검출
```
contours, _ = cv2.findContours(thresh_adaptive, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_result = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 2)
```
1. cv2.RETR_EXTERNAL: 외곽 윤곽선만 검출

2. cv2.drawContours(): 윤곽선을 이미지에 그리기

## ✅ 7. 결과 저장 코드
```
now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f"plate_{now}.png"
filepath = os.path.join(output_dir, filename)
cv2.imwrite(filepath, result_blurred)

contour_filename = f"plate_{now}_contour.png"
contour_filepath = os.path.join(output_dir, contour_filename)
cv2.imwrite(contour_filepath, contour_result)
```

## ✅ 8. 핵심 요약
| 처리 단계  | 사용 함수                                           | 효과       |
| ------ | ----------------------------------------------- | -------- |
| 그레이스케일 | `cv2.cvtColor`                                  | 컬러 → 흑백  |
| 블러링    | `GaussianBlur`, `medianBlur`, `bilateralFilter` | 노이즈 제거   |
| 모폴로지   | `morphologyEx`                                  | 잡음/구멍 제거 |
| 이진화    | `adaptiveThreshold`                             | 문자 강조    |
| 윤곽선    | `findContours`, `drawContours`                  | 문자 영역 탐지 |













