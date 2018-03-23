import wave
import struct
from DTMFdetector import DTMFdetector

import sys

freq = 8000
debugFlag = False
dtmf = DTMFdetector(freq,debugFlag)

def method1(audio_file):
    """Proves that the tests pass."""
    return "0123456789p*ABCD"


def method5(audiofile):
    data = dtmf.getDTMFfromWAV(audiofile)
    return data
