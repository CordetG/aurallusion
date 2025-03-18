#!/usr/bin/python3

from .default_colors import *
import numpy as np
import colorsys

class Color:
    '''Create a color using the visible light spectrum and luminosity.
    -----------
    Attributes:
        hue -- Normalized hue of degree value
        sat -- Normalized saturation of a percent value
        lum -- Normalized Brightness of a percent value
    '''

    def __init__(self, color_attribute: list) -> None:
        self.hue = color_attribute[0]
        self.sat = color_attribute[1]
        self.lum = color_attribute[2]
    # end __init__ def
    
    def read_data(self):
        pass
    # end def
    
    def create_color(self):
        pass
    # end def
    
    def adjust_luminosity(self):
        pass
    # end def
    
    def calculate_color_with_lum(self):
        pass
    # end def
    
    def convert_to_rgb(self):
        pass
    # end def
    
    def read_data():
        pass
    # end def
    
    def create_color():
        pass
    # end def
    
    def adjust_luminosity():
        pass
    # end def
    
    def calculate_color_with_lum():
        pass
    # end def
    
    def convert_to_rgb():
        pass
    # end def
    
# end class