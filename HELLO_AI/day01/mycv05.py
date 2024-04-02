import cv2

img = cv2.imread('iu.png')



(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated_45 = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Rotated by 45 Degrees", rotated_45)

print(img)

cv2.waitKey(0)
