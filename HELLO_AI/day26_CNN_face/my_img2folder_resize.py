import cv2

arr = [
    {'lbl':'0','f':'00','n':'박주호'},
    {'lbl':'1','f':'01','n':'박지원'},
    {'lbl':'2','f':'02','n':'이미소'},
    {'lbl':'3','f':'03','n':'하예종'}
]
    
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def mp4Toimg(myname,folderName):
    video = cv2.VideoCapture(f'img/{myname}.mp4')

    frame_count = 0
    while(video.isOpened()) :
        ret, frame = video.read()
        if ret :
            frame_count += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3,5)
            for (x,y,w,h) in faces:
                cropped = frame[y:y+h, x:x+w]
                cropped = cv2.resize(cropped,(32,32))
                cv2.imwrite(f'pre01/{folderName}/{frame_count}.png',cropped)
        else :
            break;

for a in arr:
    mp4Toimg(a['n'], a['f'])
