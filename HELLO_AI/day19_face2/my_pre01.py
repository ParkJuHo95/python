import cv2

video = cv2.VideoCapture('img/박주호.mp4')

frame_count = 0
while(video.isOpened()) :
    ret, frame = video.read()
    
    if ret :
        frame_count += 1
        cv2.imwrite(f'pre01/{frame_count}.png',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()



