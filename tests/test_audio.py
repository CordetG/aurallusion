from utils.audiokit import sound
import numpy as np

wavObj = sound.Wave(
    channelsPerFrame=1,
    sampleSizeBits="np.int16",
    amplitude=0.25,
    duration=1,
    frequency=440,
    sampleRate=48000,
    wavName="sine.wav"
)

def test_sine_wave_equation_at_t_0() -> None:
    
    sineResult = wavObj.sineWave(time=0)
    expectedValue = 0

    assert sineResult == expectedValue, "Sine equation should return 0"
# end def test


# Run Testing
# In root directory, run python3 -m tests.test_audio
if __name__ == "__main__":
    test_sine_wave_equation_at_t_0()
    print("Audio Testing Passed!")
# end if