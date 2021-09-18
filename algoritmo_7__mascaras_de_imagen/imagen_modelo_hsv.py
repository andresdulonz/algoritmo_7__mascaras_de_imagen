import cv2
import numpy as np

# Separación de canales HSV
h = np.zeros((480,640),dtype=np.uint8) + 58
s = np.zeros((480,640),dtype=np.uint8) + 252
v = np.zeros((480,640),dtype=np.uint8) + 214

hsv = cv2.merge((h,s,v))
img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('Imagen',img)
cv2.waitKey(0)