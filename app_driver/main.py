#!/usr/bin/python3

# driver to communicate between frontend & backend

from utils.core_data import eval
from utils.mlsignals import tree
from ui import input_window
import tkinter as tk
from utils.audiokit import sound
import matplotlib

def main() -> int:
    return 0

# end main

test_set = {
    17 : 0,
    524 : 5,
    70 : 2,
    350 : 4
    }

note_set = {
    17 : 0,
    524 : 0,
    70 : 1,
    350 : 5
    }

file_name =  {
    17 : 'test_1',
    524 : 'test_2',
    70 : 'test_3',
    350 : 'test_4'
    }


def run_ml_utils(model, freq, octave, note):
    return model.predict([[freq, octave, note]])[0]
# end def

def run_input_window() -> None:
    
    in_win_obj = input_window.InterfaceWindow('b29bc1')
    in_win_obj.create_input_window()
    in_win_obj.display_window_title()
    in_win_obj.display_specs()
    in_win_obj.input_box()
    in_win_obj.window_button()
    in_win_obj.run_window()
    
    return in_win_obj.copy_input()
#end def test

def run_audio(freq_input, file_name):
    wavObj = sound.Wave(
        channelsPerFrame=1,
        sampleSizeBits="np.int16",
        amplitude=0.25,
        duration=1,
        frequency=freq_input,
        sampleRate=48000,
        wavName=f'{file_name}.wav'
    )
    
    sampleArray = wavObj.generateSamples()
    wavObj.writeWav(wavData=sampleArray)
    wavObj.playAudio(audioData=sampleArray)
    
def output_color(bg):
    in_win_obj = input_window.InterfaceWindow(bg)
    in_win_obj.create_input_window()
    in_win_obj.display_window_title()
    in_win_obj.run_window()
    
    
# https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/   
def convert(rgb):
    return '%02x%02x%02x' % int(rgb)

# Run Testing
# In root directory, run python3 -m app-driver.main
if __name__ == "__main__":
    ml_model_obj = tree.DecisionTreeModel()
    model = ml_model_obj.load_trained_data()
    
    frequency = int(run_input_window())
    r, g, b = run_ml_utils(model, frequency, test_set[frequency], note_set[frequency])
    hex = matplotlib.colors.to_hex([ r/255, g/255, b/255 ])
    
    
    output_color(hex)
    
    run_audio(frequency, file_name[frequency])
