import cv2

img = cv2.imread('dong.jpg')

cv2.putText(img, "Dong", (300,150), cv2.FONT_ITALIC, 2, (255,0,0), 1)

cv2.imshow('image',img)
cv2.waitKey()

#putText는 한글인식을 못해서 깨진다.