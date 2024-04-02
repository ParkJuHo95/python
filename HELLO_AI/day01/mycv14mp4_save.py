import cv2

cap = cv2.VideoCapture('sarang.mp4')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('wars.mp4', fourcc, 30.0, (int(width), int(height)))

while(cap.isOpened()) :
    ret, frame = cap.read()
    
    if ret :
        cv2.imshow('frame', frame)
        out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()