# 얼굴인식후 모자이크 처리 : 익명화
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 얼굴 검출
face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')

img = cv2.imread('./img/smilings.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

# 얼굴 검출 후 모자이크
for x,y,w,h in faces:
    roi = img[y:y+h, x:x+w]
    roi = cv2.resize(roi, (w//5, h//5)) # 여기로 정도를 수정
    roi = cv2.resize(roi, (w, h))
    img[y:y+h, x:x+w] = roi



img_pil = Image.fromarray(img)
font = ImageFont.truetype("malgun.ttf", 40)  # 경로 수정 필요
draw = ImageDraw.Draw(img_pil)
draw.text((50, 300), "2021143016 이장헌", font=font, fill=(0, 255, 0, 0))
img = np.array(img_pil)

cv2.imshow('img',img)
cv2.imshow('gray', gray)
cv2.waitKey()
cv2.destroyAllWindows()