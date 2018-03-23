import unittest
import os
from dtmfa import parse
import re

class TestDTMF(unittest.TestCase):

    # def test_dtmf_tones(self):
    #     """Sample DTMF tone sends a string, DTMF should detect string"""
    #     input = "0123456789p*ABCD"
    #     sample = "/Users/aloughran/Code/Hackathon/audio/output16.wav"
    #     result = parse.method1(sample)
    #     assert result == input

    # def test_dtmf_tone(self):
    #     """Sample DTMF tone sends a string, DTMF should detect string"""
    #     input = "708078"
    #     sample = "/Users/aloughran/Code/Hackathon/audio/708078.wav"
    #     result = parse.method5(sample)
    #     assert result == input

    # def test_dtmf_tone_broken(self):
    #     """Sample DTMF tone sends a string, DTMF should detect string"""
    #     input = "708078"
    #     sample = "/Users/aloughran/Code/Hackathon/audio/brokenoutput.wav"
    #     result = parse.method5(sample)
    #     assert result == input

    # def test_dtmf_tone_309738(self):
    #     """Sample DTMF tone sends a string, DTMF should detect string"""
    #     input = "309738"
    #     sample = "/Users/aloughran/Code/Hackathon/audio/309738.wav"
    #     result = parse.method5(sample)
    #     assert result == input

    def test_all_audiofiles(self):
        """Tests all audio files in the audio folder"""
        cwd = os.getcwd()
        results = []
        for filename in os.listdir('audio/'):
            expected = re.split('.wav', filename)[0]
            testfile = cwd + "/audio/" + filename
            result = parse.method5(testfile)
            if (expected == result):
                results.append(filename)
                results.append(True)
            else:
                results.append(filename)
                results.append(False)
                print("Expected: %s, Received: %s" % (expected, result))
        assert(False not in results)

        
        
