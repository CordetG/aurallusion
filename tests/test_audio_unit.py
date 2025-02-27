from utils.audiokit import sound
import numpy as np
import unittest

wavObj = sound.Wave(
    channelsPerFrame=1,
    sampleSizeBits="np.int16",
    amplitude=0.25,
    duration=1,
    frequency=440,
    sampleRate=48000,
    wavName="sine.wav"
)

class TestSoundMethods(unittest.TestCase):

    def test_sine_at_t_0(self):
        sineResult = wavObj.sineWave(time=0)
        self.assertEqual(sineResult, 0)
        self.assertFalse(sineResult != 0)
    # end def

    def test_generate_samples(self):
        sampleArray = wavObj.generateSamples()
        self.assertEqual(sampleArray.dtype, np.dtype('int16'))
    # end def
# end class

# run 'python -m unittest tests/test_audio.py'
# coverage data: run 'python -m coverage run -m unittest'
#   then run 'python -m coverage report'
if __name__ == '__main__':
    unittest.main()