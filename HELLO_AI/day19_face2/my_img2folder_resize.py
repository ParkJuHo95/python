import cv2

arr = [
    {'lbl':'0','f':'00','n':'김민경'},
    {'lbl':'1','f':'01','n':'김승연'},
    {'lbl':'2','f':'02','n':'김차은'},
    {'lbl':'3','f':'03','n':'김창용'},
    {'lbl':'4','f':'04','n':'김초희'},
    {'lbl':'5','f':'05','n':'김현우'},
    {'lbl':'6','f':'06','n':'남희수'},
    {'lbl':'7','f':'07','n':'박주호'},
    {'lbl':'8','f':'08','n':'박지원'},
    {'lbl':'9','f':'09','n':'배유림'},
    {'lbl':'10','f':'10','n':'백영웅'},
    {'lbl':'11','f':'11','n':'변상원'},
    {'lbl':'12','f':'12','n':'송은비'},
    {'lbl':'13','f':'13','n':'우민규'},
    {'lbl':'14','f':'14','n':'유길상'},
    {'lbl':'15','f':'15','n':'이미소'},
    {'lbl':'16','f':'16','n':'이상철'},
    {'lbl':'17','f':'17','n':'이성휘'},
    {'lbl':'18','f':'18','n':'정민지'},
    {'lbl':'19','f':'19','n':'하예종'}
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

mp4Toimg("박주호","07")
    
    
# for a in arr:
#     mp4Toimg(a['n'], a['f'])
    # print(a['lbl'])
    # print(a['n'])
    # print(a['f'])
