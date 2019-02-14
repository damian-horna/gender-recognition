from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
from scipy.signal import kaiser, decimate
import math as mt
from os import listdir
import scipy.io.wavfile
import warnings
import sys

warnings.filterwarnings("ignore")

wav = str(sys.argv[1])
try:
	w, signal = scipy.io.wavfile.read(wav)
	
	try:
		signal = [s[0] for s in signal] #first channel only
	except:
		#do nothing
		signal = signal
		
	try:
		signal = signal[w:2*w]
	except:
		signal = signal[w:]
		
	spec = abs(fft(signal))
	hps = copy(spec)
	for h in np.arange(2, 5):
		dec = decimate(spec, h)
		hps[:len(dec)] *= dec
	duration = int(len(signal)/w) #in seconds
	offset = 70 * duration
	highestFreq = np.argmax(hps[offset:])
	freq = (offset + highestFreq) / duration
	
	if freq < 175:
		print("M")
	else:
		print("K")
except: 
	print("K")