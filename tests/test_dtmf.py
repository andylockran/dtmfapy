import unittest

from dtmfa import parse

class TestDTMF(unittest.TestCase):

    def test_dtmf_tones(self):
        """Sample DTMF tone sends a string, DTMF should detect string"""
        input = "0123456789p*ABCD"
        sample = "/Users/aloughran/Code/Hackathon/audio/output16.wav"
        result = parse.method1(sample)
        assert result == input

    def test_dtmf_tone(self):
        """Sample DTMF tone sends a string, DTMF should detect string"""
        input = "708078"
        sample = "/Users/aloughran/Code/Hackathon/output.wav"
        result = parse.method5(sample)
        assert result == input
