import cv2

image = cv2.imread('k.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for idx, (x, y, w, h) in enumerate(faces):
    #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cropped = image[y:y+h, x:x+w]
    cv2.imshow(f"{idx}", cropped)
    cv2.imwrite(f"{idx}.png", cropped)
    print(idx,x, y, w, h)

cv2.imshow('Face Detection', image)
cv2.waitKey()
cv2.destroyAllWindows()

