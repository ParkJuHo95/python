import cv2

img = cv2.imread('sukgu.jpg')

x,y,w,h = cv2.selectROI(img, False)
roi = img[y:y+h, x:x+w]
roi = cv2.resize(roi, (w//20, h//20))
roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
img[y:y+h, x:x+w] = roi

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
