import cv2

img = cv2.imread('k.jpg')
x = 100
y = 100
w = 100
h = 100
cropped_img = img[y:y+h,x:x+w]


cv2.imshow('k',img)
cv2.imshow('k_c',cropped_img)

cv2.waitKey()
cv2.destroyAllWindows()