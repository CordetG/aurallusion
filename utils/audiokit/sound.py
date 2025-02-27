#!/usr/bin/python3

# Referenced from sine wave assignment
# from Spring Term 2023 CS510 Music, Sound, and Computers class

from scipy.io import wavfile as scwave
import math
import numpy as np
import sounddevice as sdevice

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
            wavName) -> None:
        
        self.channelsPerFrame: int = int(channelsPerFrame)
        self.sampleSizeBits = eval(sampleSizeBits)
        self.amplitude: int = int(float(amplitude) * np.iinfo(self.sampleSizeBits).max)
        self.duration: int = int(duration)
        self.frequency: int = int(frequency)
        self.sampleRate: int = int(sampleRate)
        self.waveName: str = wavName
    # end def
    
    '''Sinusoidal equation at time (t): s(t)=a*sin(2pi*freq*t)'''
    def sineWave(self, time) -> int:
        return int(
                self.amplitude 
                * math.sin(((2*math.pi) 
                * self.frequency)
                * (time/self.sampleRate)))
    # end def
    
    # TODO: Extend function to create samples from any generic wave.
    '''Generates sinusoidal wave as array of samples'''
    def generateSamples(self) -> np.ndarray:
        
        totalSamples: int = self.duration * self.sampleRate
        sampleList = np.empty(shape=totalSamples, dtype=np.int16)
        
        for t in range(totalSamples):
            
            newSampleData: int = self.sineWave(t)
            sampleList[t] = newSampleData
        # end for
        
        return sampleList
    # end def
    
    '''Write the .wav files'''
    def writeWav(
        self, 
        wavData) -> None:
        directory = './assets'  # Replace with your desired directory
        filename = self.waveName
        full_path = f'{directory}/{filename}'
        
        scwave.write(
            full_path,
            rate=self.sampleRate, 
            data=wavData
        )
    # end def
    
    '''Play Audio directly to computer speakers'''
    def playAudio(self, audioData) -> None:
        
        print("Playing ", self.waveName.replace('.wav', ''), " data...")
        sdevice.play(data=audioData, samplerate=self.sampleRate, blocking=True)
    # end def
    
# end class

