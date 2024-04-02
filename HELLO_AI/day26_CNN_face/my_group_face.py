import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from day26_CNN_face.my_pred_oop import AiFace


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('team.jpg')
font=ImageFont.truetype("fonts/gulim.ttc",15)
af = AiFace()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),3)
    cropped = img[y:y+h, x:x+w]
    name = af.getNameByImage(cropped)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)  
    draw.text((x+w/2-20,y-20),name,font=font,fill=(255,255,0))
    img = np.array(img)

cv2.imshow("team",img)
cv2.waitKey(0)
cv2.destroyAllWindows()