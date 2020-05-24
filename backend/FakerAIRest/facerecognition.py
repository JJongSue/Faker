import numpy as np
import cv2
import base64
from matplotlib import pyplot as plt
from PIL import Image
import io
import face_recognition


'''
박종수 20200524
얼굴의 위치를 찾아서 base64의 list로 반환해주는 함수
'''
def find_location(base64_img):
    #인터넷에서 얻은 base64는 앞에 jpeg,로 구분되어 들어가서 이를 split으로 나눔
    base64_img = base64_img.split(',')
    base64_img = base64_img[1]

    #인코딩 된 이미지 PIL.image를 nparray로 변환후 face_locations함수를 이용해 얼굴 위치 찾음
    encoding_img = base64.b64decode(encoding_img)
    image = Image.open(io.BytesIO(i))
    image_np = np.array(image)
    face_locations = face_recognition.face_locations(image_np)

    images = []
    for (top, right, bottom, left) in face_locations:
        return_img = image.crop((left, top, right, bottom))
        return_img =base64.b64encode(return_img.tobytes())
        images.append(str(return_img))
    return images