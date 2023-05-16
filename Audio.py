import numpy as np
import sounddevice as sd
import soundfile as sf
from matplotlib import pyplot as plt

s, fs = sf.read("audio.wav", dtype="float32")
countSamples=len(s[:0])
time=np.array(range(countSamples)*(1/fs))
plt.plot(fs[0],time)

frames=np.zeros((fs/441,441))
k=0
for i in range(fs/441):
    for j in range(441):
        frames[i][j]=s[k][0]
        k+=1