import cv2
import os


TARGER_DIR = '/home/navaneeth/work/oneon/detected'
epoches = 3
image = cv2.imread("/home/navaneeth/work/oneon/test.jpg")
h1 = 100
w1 = 100


def rotate(image):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    rotate_imgs = os.path.join(TARGER_DIR, "rota_" + str(i) + ".png")
    cv2.imwrite(rotate_imgs, rotated)


def resize(image):
    r = h1/image.shape[1]
    dim = (w1, int(image.shape[0]*r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    resiz_imgs = os.path.join(TARGER_DIR, "resiz_" + str(i) + ".png")
    cv2.imwrite(resiz_imgs, resized)


for i in range(epoches):
    rotate(image)
    resize(image)
    h1 = h1*2
    w1 = w1*2
    i = i+1
