import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = np.full((500,500,3), 255, dtype=np.uint8)

# sans_serif small
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0))
# sans_serif normal
cv2.putText(img, "Simplex", (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
# san_serif bold
cv2.putText(img, "Duplex", (50,110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))
# san_serif normal
cv2.putText(img, "Simplex X 2", (200,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0))

# serif small
cv2.putText(img, "Serif Plain", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,0,0))
# serif normal
cv2.putText(img, "Serif normal", (50,220), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
# serif bold
cv2.putText(img, "serif bold", (50,260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
# serif normal X 2
cv2.putText(img, "Serif Plain X 2", (200,260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0))

# 한글 표시
img_pil = Image.fromarray(img)
font = ImageFont.truetype("malgun.ttf", 40)  # 경로 수정 필요
draw = ImageDraw.Draw(img_pil)
draw.text((50, 300), "이장헌 제작", font=font, fill=(0, 255, 0, 0))
img = np.array(img_pil)


cv2.imshow("text", img)
cv2.waitKey()
cv2.destroyAllWindows()
