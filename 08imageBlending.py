# 2025.10.22
# 2025년 2학기 이미지 처리 수업
# 08 image blending
# - 여러개의 이미지를 덧셈, 뺄셈 등의 연산을 통해 이미지를 합성한다.

# 1. 이미지의 덧셈
import cv2
import numpy as np

img1 = cv2.imread('./image_samples/wing_wall.jpg')
img2 = cv2.imread('./image_samples/yate.jpg')

img3 = img1 + img2 # 더하기 연산
img4 = cv2.add(img1, img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("add", img3)
cv2.imshow("cvadd", img4)

cv2.waitKey()
cv2.destroyAllWindows()

# 이미지의 합성을 웨이트로 처리 (alpha)
alpha = 0.7
blended_img = img1 * alpha + img2 * (1-alpha)
blended_img = blended_img.astype(np.uint8)

blended_cv = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)

cv2.imshow("blended_img", blended_img)
cv2.imshow("blended_cv", blended_cv)
cv2.waitKey()
cv2.destroyAllWindows()

# 가변 웨이트로 두 이미지를 합성함
img1 = cv2.imread('./image_samples/man_face.jpg')
img2 = cv2.imread('./image_samples/lion_face.jpg')


win_name = 'blending'
def onChgage(x):
    alpha = x / 100
    dst = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)
    cv2.imshow(win_name, dst)

cv2.imshow(win_name, img1)
cv2.createTrackbar('fade', 'blending', 0, 100, onChgage)

cv2.waitKey()
cv2.destroyAllWindows()
