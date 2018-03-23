import pyaudio
import wave
import argparse
#from pydub import AudioSegment

import parse

from DTMFdetector import DTMFdetector

import sys

freq = 8000
debugFlag = True
dtmf = DTMFdetector(freq,debugFlag)

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 1
RECORD_SECONDS = 7
WAVE_OUTPUT_FILENAME = "output.wav"
 

def listen():
    """Listens for 3 seconds for audio"""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print "recording..."
    frames = []
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    return WAVE_OUTPUT_FILENAME

# def quieter(audiofile):
#     song = AudioSegment.from_wav(audiofile)
#     song = song + 20
#     song.export("quieter.wav", "wav")
#     return "quieter.wav"

def static_main():
    """ Runs the main program """
    audiodata = listen();
    #audiodata = quieter('output.wav') ## Used to reduce the dB of the audio.. Not really required now
    return parse.method5(audiodata)
    #return True

def main():
    """ Listens dynamically"""
    data = dtmf.getDTMFLive()


def parseFile(filename):
    returnparse.method5(filename)
    return True


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Copy Seed Data"
    )

    parser.add_argument(
        "-f",
        "--filename",
        help="The filename to parse",
        type=str
    )

    args = parser.parse_args()
    print(args)
    if not (vars(args))['filename']:
        dynamic_main();
    else:
        filename = (vars(args))['filename']
        parseFile(filename)

    
