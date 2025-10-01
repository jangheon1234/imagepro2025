# 얼굴인식 프로젝트
# opencv Harr filter를 연속적용하는 방식
# 2025.10.01
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 얼굴 검출
face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')

# 눈 검출
eyes_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')

img = cv2.imread('./img/smilings.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

# [[146  96 120 120] = [x,y,w,h] => (x, y), (x+w, y+h)
#  [398  97 106 106]] = [x,y,w,h]

# boy_face.jpg
# [[146 190 306 306]]

# print(faces)

#children.jpg
# cv2.rectangle(img, (146,96), (120+146,120+96), (255,0,0), 5)
# cv2.rectangle(img, (398,97), (106+398,106+97), (0,255,0), 5)
# boy
# cv2.rectangle(img, (146, 190), (306+146,306+190), (255,0,0), 5)

# for face in faces:
#     fx, fy, fw, fh = face
#     cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 3)

for x,y,w,h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
    eyes = eyes_cascade.detectMultiScale(gray[y:y+h, x:x+w])
    for ex, ey, ew, eh in eyes:
        cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 0, 255), 1)


img_pil = Image.fromarray(img)
font = ImageFont.truetype("malgun.ttf", 40)  # 경로 수정 필요
draw = ImageDraw.Draw(img_pil)
draw.text((50, 300), "2021143016 이장헌", font=font, fill=(0, 255, 0, 0))
img = np.array(img_pil)

cv2.imshow('img',img)
cv2.imshow('gray', gray)
cv2.waitKey()
cv2.destroyAllWindows()