import cv2

im = cv2.imread('ejercicio5.png')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(55,253,235),(59,255,239))

cv2.imshow('Imagen 1.5. cv2.inRange(hsv,(55,253,235),(59,255,239))', mask)
cv2.waitKey(0)