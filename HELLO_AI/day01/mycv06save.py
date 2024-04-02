import cv2

img = cv2.imread('iu.png')

cv2.imshow('image',img)
cv2.imwrite("result.jpg", img)

cv2.waitKey()
print(img)