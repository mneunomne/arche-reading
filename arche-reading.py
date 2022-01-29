# -*- coding: UTF-8 -*-

# Arche Writings libs
import pyaudio
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
from playsound import playsound

# arche writing 8bit alphabet
alphabet = list('撒健億媒間増感察総負街時哭병体封列効你老呆安发は切짜확로감外年와모ゼДが占乜산今もれすRビコたテパアEスどバウПm가бうクん스РりwАêãХйてシжغõ小éजভकöলレ入धबलخFসeवমوযиथशkحくúoनবएদYンदnuনمッьノкتبهtт一ادіاгرزरjvةзنLxっzэTपнлçşčतلイयしяトüषখথhцहیরこñóহリअعसमペيフdォドрごыСいگдとナZকইм三ョ나gшマで시Sقに口س介Иظ뉴そキやズВ자ص兮ض코격ダるなф리Юめき宅お世吃ま来店呼설진음염론波密怪殺第断態閉粛遇罩孽關警')

PyAudio = pyaudio.PyAudio     
SAMPLERATE = 8000

def openSampleData ():
  with open('sample_data/354.txt', encoding='utf-8') as f:
    data = f.read()
    numbers=[]
    for c in list(data):
      n = alphabet.index(c)
      numbers.append(n)
    # write and play audio
    playWavedata(numbers)

# detections are structured in the following way:
# [[x, y, w, h, class_int]]
def playDetections(detections):
  wavedata = ''
  # Arche Writing: Process detectiosn
  sorted(detections, key=lambda k: [k[1], k[0]])
  numbers=[]
  for d in detections:
      wavedata = wavedata+chr(d[4])
      numbers.append(d[4])
  playWavedata(numbers)

# play wavedata as a string of chr(d[4])
def playWavedata (numbers, sample_rate=SAMPLERATE):
  wavedata = np.asarray(numbers).astype(np.int8)

  write("temp.wav", sample_rate, wavedata)
  playsound('temp.wav')


openSampleData()