import cv2

cap = cv2.VideoCapture('sarang.mp4')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
face_mask = cv2.imread('./mask/118.png',cv2.IMREAD_UNCHANGED)

mask=face_mask[:,:,-1] 
face_mask=face_mask[:,:,0:3]
print(mask.shape)

while(cap.isOpened()) :
    ret, frame = cap.read() 
    
    if ret :
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        factor = 20
        for idx, (x, y, w, h) in enumerate(faces):
            face_mask=  cv2.resize(face_mask,(w, h),interpolation = cv2.INTER_AREA)
            mask = cv2.resize(mask, (w,h), interpolation=cv2.INTER_AREA)
            crop = frame[y:y+h, x:x+w]
            cv2.copyTo(face_mask,mask,crop)
            
        cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


