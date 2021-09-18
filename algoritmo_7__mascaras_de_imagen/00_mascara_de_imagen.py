import cv2

im = cv2.imread('Captura.PNG')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(69,0,0),(69,255,255))

cv2.imshow('Imagen', mask)
cv2.waitKey(0)