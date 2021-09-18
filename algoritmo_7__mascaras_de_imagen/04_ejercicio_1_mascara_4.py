import cv2

im = cv2.imread('ejercicio4.png')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(160,143,165),(163,147,167))

cv2.imshow('Imagen 1.4. cv2.inRange(hsv,(160,143,165),(163,147,167)', mask)
cv2.waitKey(0)