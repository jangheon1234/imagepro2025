# 직선 그리기

import cv2
import numpy as np

# RGB = 각각 255로 초기화 , 흰색 [198, 47, 185]
img = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.line(img, (100,50), (250,50), (0,0,255))
cv2.line(img, (200,50), (350,50), (0,255,0))
cv2.line(img, (300,50), (450,50), (255,0,0))

cv2.line(img, (100,100), (400,100), (255,25,0), 10)
cv2.line(img, (100,150), (400,150), (55,255,0), 10)
cv2.line(img, (100,200), (400,200), (2,25,0), 10)
cv2.line(img, (100,250), (400,250), (22,115,12), 10)
cv2.line(img, (100,300), (400,300), (15,45,222), 10, cv2.LINE_AA)

# AA : Anti Aliasing
cv2.line(img, (100,350), (400,350), (0,0,255), 20, cv2.LINE_4)
cv2.line(img, (100,400), (400,400), (0,0,255), 20, cv2.LINE_8)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
