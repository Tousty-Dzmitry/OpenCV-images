import numpy as np
import cv2

img = cv2.imread('1.jpg', 0)

# изменить размер изобржения

wide = 300
f = float(wide) / img.shape[1]

new_size = (wide, int(img.shape[0]*f))

new_img = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

# поворот избражения




cv2.imshow('cnn-1', new_img)
# cv2.imshow('CNN', img)
cv2.waitKey(0)
cv2.destroyAllWindows()