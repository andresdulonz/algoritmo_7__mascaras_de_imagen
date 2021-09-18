import cv2

im = cv2.imread('ejercicio1.png')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(150,0,0),(150,255,255))

cv2.imshow('Imagen 1.1. cv2.inRange(hsv,(150,0,0),(150,255,255))', mask)
cv2.waitKey(0)