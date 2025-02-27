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

def test_generate_samples_and_writes_and_plays_samples_as_audio() -> None:
    
    sampleArray = wavObj.generateSamples()
    wavObj.writeWav(wavData=sampleArray)
    wavObj.playAudio(audioData=sampleArray)
#end def test

# Run Testing
# In root directory, run python3 -m tests.test_audio
if __name__ == "__main__":
    test_generate_samples_and_writes_and_plays_samples_as_audio()
    print("Audio Testing Passed!")
# end if