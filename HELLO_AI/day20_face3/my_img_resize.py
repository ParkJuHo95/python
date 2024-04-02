import cv2


img = cv2.imread("team.jpg")
img = cv2.resize(img,(1000,750))
cv2.imwrite("resize.jpg",img)