import pyaudio
import wave

from pydub import AudioSegment

import parse

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 1024
RECORD_SECONDS = 5
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

    song = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
    song = song - 20
    song.export("quieter.wav", "wav")
    return "output.wav"



def main():
    """ Runs the main program """
    audiodata = listen();
    #audiodata = "output.wav"
    print(parse.method5(audiodata))
    return True
    


if __name__ == "__main__":
    main();
