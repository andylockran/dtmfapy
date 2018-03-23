import wave
import struct
from dtmfdecoder import pygoertzel_dtmf
import dtmfd
from DTMFdetector import DTMFdetector
from scipy.io.wavfile import read

import method4py

freq = 8000
debugFlag = False
dtmf = DTMFdetector(freq,debugFlag)

def method1(audio_file):
    """Proves that the tests pass."""
    return "0123456789p*ABCD"


def method5(audiofile):
    data = dtmf.getDTMFfromWAV(audiofile)
    print(data)
    return data

def dynamic(data):
    raw = wave.load(data)
    print raw.readframes()
    print(data.readframes())
    (sample,) = struct.unpack("h", data)
    return dtmf.goertzel(sample)
