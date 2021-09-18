import cv2

im = cv2.imread('ejercicio3.png')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(87,81,142),(89,83,144))

cv2.imshow('Imagen 1.3. cv2.inRange(hsv,(87,81,142),(89,83,144))', mask)
cv2.waitKey(0)