import cv2

webcam = cv2.VideoCapture(0)
cnt = 0
if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    
    myKey = cv2.waitKey(1)
    
    if status:
        cv2.imshow("test", frame)
        
    if myKey == 97 :
        cv2.imwrite(f'{cnt}.png', frame)
        cnt += 1
    if myKey == 113 :
        break;

webcam.release()
cv2.destroyAllWindows()