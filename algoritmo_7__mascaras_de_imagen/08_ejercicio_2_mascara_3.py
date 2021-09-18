import cv2

im = cv2.imread('proyector.jpg')
hsv= cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask= cv2.inRange(hsv,(30,50,50),(120,255,255))

cv2.imshow('Imagen 2.3. cv2.inRange(hsv,(30,50,50),(120,255,255))', mask)
cv2.waitKey(0)