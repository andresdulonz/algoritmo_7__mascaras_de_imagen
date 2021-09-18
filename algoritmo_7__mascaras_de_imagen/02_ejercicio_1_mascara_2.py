import cv2

im = cv2.imread('ejercicio2.png')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(27,0,0),(27,255,255))

cv2.imshow('Imagen 1.2. cv2.inRange(hsv,(27,0,0),(27,255,255))', mask)
cv2.waitKey(0)