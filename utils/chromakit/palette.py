#!/usr/bin/python3

from .color import *
from .default_colors import *
import numpy as np
import colorsys

class ColorPalette:
    '''Create an array of colors.
    -----------
    Attributes:
        colors -- list of colors represented as (r,g,b) values
    '''
    
    def __init__(self) -> None:
        self.colors: list[int] = []
    # end __init__ def
    
    def add_base_colors():
        pass
    # end def
    
    def add_greyscale():
        pass
    # end def
    
    def add_scaled_colors():
        pass
    # end def
    
    def copy_color_vectors():
        pass
    # end def
    
# end class