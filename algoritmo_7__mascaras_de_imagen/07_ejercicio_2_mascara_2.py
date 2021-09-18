import cv2

im = cv2.imread('camara_2.jpg')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(64,250,166),(68,254,170))

cv2.imshow('Imagen 2.2 cv2.inRange(hsv,(64,250,166),(68,254,170))', mask)
cv2.waitKey(0)