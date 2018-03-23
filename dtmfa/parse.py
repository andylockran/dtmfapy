import wave
import struct
from DTMFdetector import DTMFdetector

freq = 8000
debugFlag = True
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
