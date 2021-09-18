import cv2

im = cv2.imread('camara.jpg')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(30,200,100),(80,255,255))
# mask= cv2.inRange(hsv,(53,250,212),(62,255,138))
cv2.imshow('Imagen 2.1 cv2.inRange(hsv,(30,200,100),(80,255,255))', mask)
cv2.waitKey(0)