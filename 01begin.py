import cv2

img_file = "image_samples/girl.jpg"
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')

# 2025.09.17 pillow를 사용한 이미지 보기
# 단순하게 이미지를 보여주는 경우는 PIL 사용 추천
from PIL import Image
img = Image.open("./image_samples/boy_face.jpg").show()

# 흑백으로 읽기
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')

# 동영상 읽기
video_file = "./image_samples/big_buck.avi"
cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(1)
        else:
            break
else:
    print("cannot open video")
cap.release()
cv2.destroyAllWindows()

