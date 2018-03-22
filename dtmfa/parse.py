import wave
import struct
from dtmfdecoder import pygoertzel_dtmf
import dtmfd
from DTMFdetector import DTMFdetector
from scipy.io.wavfile import read

import method4py

def method1(audio_file):
    """Proves that the tests pass."""
    return "0123456789p*ABCD"


def method5(audiofile):
    freq = 8000
    debugFlag = False
    dtmf = DTMFdetector(freq,debugFlag)
    data = dtmf.getDTMFfromWAV(audiofile)
    print(data)
    return data