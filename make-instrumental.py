from pygame import mixer
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile

file = 'could-heaven.mp3'

fs, data = wavfile.read(file)

mixer.init()
mixer.music.load(file)
mixer.music.play()

import time
while mixer.music.get_busy():
    time.sleep(0.1)
