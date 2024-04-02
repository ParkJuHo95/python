import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# y, sr = librosa.load("곽금규가4.mp3")
y, sr = librosa.load("animal/박주호/00.wav")
# y, sr = librosa.load("taehyun1.wav")

t = np.arange(0, len(y))

print(t)
print(y)
print(len(t))
print(len(y))

sr = np.ones((200))

plt.plot(t,y)
plt.grid()
plt.savefig('wave.png')
plt.show()



