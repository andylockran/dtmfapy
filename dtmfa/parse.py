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


def method2(audio_file):
    """Simplest method: http://johnetherton.com/projects/pys60-dtmf-detector/"""
    dtmf = DTMFdetector()
    data = dtmf.getDTMFfromWAV(audio_file)
    print(type(data))
    print(data)
    return data


def method3(audio_file):
    """Runs, but more complex: """
    # load wav file
    wav = wave.open(audio_file, 'r')
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    frames = wav.readframes(nframes * nchannels)
    # convert wave file to array of integers
    frames = struct.unpack_from("%dH" % nframes * nchannels, frames)
    # if stereo get left/right
    if nchannels == 2:
        left = [frames[i] for i in range(0,len(frames),2)]
        right = [frames[i] for i in range(1,len(frames),2)]
    else:
        left = frames
        right = left
    binsize = 400
    # Split the bin in 4 to average out errors due to noise
    binsize_split = 4
    prevvalue = ""
    prevcounter = 0
    for i in range(0,len(left)-binsize,binsize/binsize_split):
        goertzel = pygoertzel_dtmf(framerate)
        for j in left[i:i+binsize]:
            value = goertzel.run(j)
        if value==prevvalue:
            prevcounter+=1
            if prevcounter==10:
                print(value)
        else:
            prevcounter=0
            prevvalue=value


def method4(audio_file):
    """The example Pete posted: https://gist.github.com/soravux/1ce124315bc6d1f3d430"""
    rate, data = read(audio_file)
    tones = method4py.getTones(data, rate)
    out = method4py.mergeTones(tones)
    number = method4py.decodeDTMF(out)
    print(number)