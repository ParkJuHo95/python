import cv2

img = cv2.imread('iu.png')


imageRectangle = img.copy()

cv2.rectangle(imageRectangle, 
            (120,70),
            (265,250),
            (0,255,255),
            thickness=1, 
            lineType=cv2.LINE_AA)  
cv2.imshow("image", imageRectangle) 

cv2.waitKey(0)
