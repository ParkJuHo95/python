import cv2

img = cv2.imread('common_ir.png')
img1 = cv2.imread('common_ir.png',-1)
cv2.imshow('b',img)
cv2.imshow('b',img1)

print(img)
print(img1)

cv2.waitKey()
