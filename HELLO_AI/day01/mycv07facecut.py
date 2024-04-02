import cv2




# cascade_filename = 'haarcascade_frontalface_alt.xml'
#
# cascade = cv2.CascadeClassifier(cascade_filename)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('k.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3,5)
i =0;
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    cv2.imshow("origin",img)
    cropped = img[y:y+h, x:x+w]
    cv2.imwrite(f"{i}.jpg",cropped)
    cv2.imshow(f'{i}image', cropped)
    i+=1
    
cv2.waitKey(0)
cv2.destroyAllWindows()