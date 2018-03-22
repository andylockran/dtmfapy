import unittest

from dtmfa import parse

class TestDTMF(unittest.TestCase):

    def test_dtmf_tones(self):
        """Sample DTMF tone sends a string, DTMF should detect string"""
        input = "0123456789p*ABCD"
        sample = "/Users/aloughran/Code/Hackathon/audio/output16.wav"
        result = parse.method1(sample)
        assert result == input

    def test_dtmf_tones_1(self):
        """Sample DTMF tone sends a string, DTMF should detect string"""
        input = "0123456789p*ABCD"
        sample = "/Users/aloughran/Code/Hackathon/audio/output16.wav"
        result = parse.method2(sample)
        assert result == input

    def test_dtmf_tones_2(self):
        """Sample DTMF tone sends a string, DTMF should detect string"""
        input = "0123456789p*ABCD"
        sample = "/Users/aloughran/Code/Hackathon/audio/output16.wav"
        result = parse.method3(sample)
        assert result == input

    def test_dtmf_tones_3(self):
        """Sample DTMF tone sends a string, DTMF should detect string"""
        input = "0123456789p*ABCD"
        sample = "/Users/aloughran/Code/Hackathon/audio/output16.wav"
        result = parse.method4(sample)
        assert result == input