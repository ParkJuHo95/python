import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def cutMute(arr_n,height):
    idx_f = 0
    while True:
        if arr_n[idx_f]<height:
            pass
        else:
            break
        idx_f+=1
        
    idx_f-=500
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<height:
            pass
        else:
            break
        idx_l-=1
        
    idx_l+=500
    
    return arr_n[idx_f:idx_l]


y, sr = librosa.load("20.wav")

# y_trim = y
y_trim = cutMute(y,0.05)

t = np.arange(0, len(y_trim))
print(sr)
print(y_trim)

plt.specgram(y_trim)
plt.savefig("20.jpg")
plt.title('Spectrogram Using matplotlib.pyplot.specgram() method')  
plt.show() 





