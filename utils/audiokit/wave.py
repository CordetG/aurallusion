#!/usr/bin/python3

# Referenced from sine wave assignment
# from Spring Term 2023 CS510 Music, Sound, and Computers class

from scipy.io import wavfile as scwave
import math
import numpy as np

class Wave:
    '''A wave object uses the attributes of a sound wave
    to create a .wav file and output a sound.'''

    def __init__(
            self, 
            channelsPerFrame,
            sampleSizeBits, 
            amplitude,
            duration, 
            frequency, 
            sampleRate, 
            wavName
        ) -> None:
        
        self.channelsPerFrame: int = int(channelsPerFrame)
        self.sampleSizeBits = eval(sampleSizeBits)
        self.amplitude: int = int(float(amplitude) * np.iinfo(self.sampleSizeBits).max)
        self.duration: int = int(duration)
        self.frequency: int = int(frequency)
        self.sampleRate: int = int(sampleRate)
        self.waveName: str = wavName
    # end def
    
    '''Generates sinusoidal wave given the equation:
    s(t)=a*sin(2pi*freq*t)'''
    def generateSamples(self) -> np.ndarray:
        
        totalSamples: int = self.duration * self.sampleRate
        sampleList = np.empty(shape=totalSamples, dtype=np.int16)
        
        for aSample in range(totalSamples):
            newSampleData: int = int(
                self.amplitude 
                * math.sin(((2*math.pi) 
                * self.frequency)
                * (aSample/self.sampleRate)))
            
            sampleList[aSample] = newSampleData
        # end for
        
        return sampleList
    # end def
    
# end class

