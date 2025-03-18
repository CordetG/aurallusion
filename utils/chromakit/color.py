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
    
    def copy_color(self):
        dest_hue = self.hue
        dest_sat = self.sat
        dest_lum = self.lum
        return dest_hue, dest_sat, dest_lum
    # end def

    def create_color(self, scaling=LUM_MAX) -> np.ndarray:
        grey_lum_to_mix: float = self.adjust_luminosity(optional_lum=scaling)
        self.calculate_color_with_lum(new_lum=grey_lum_to_mix)
        return self.convert_to_rgb()
    # end def

    def adjust_luminosity(self, optional_lum=LUM_MAX) -> float:
        lum_to_change = LUM_DEFAULT
        if optional_lum != LUM_MAX and optional_lum in range(LUM_MIN, LUM_MAX):
            lum_to_change = optional_lum
        # end if
        normalized_lum = round(number=(lum_to_change/255), ndigits=3)
        return normalized_lum
    # end def

    def calculate_color_with_lum(self, new_lum: float) -> float:
        hue_lum_mix = (self.lum * 2) * new_lum
        new_lum = round(number=hue_lum_mix, ndigits=3)
        self.lum = new_lum
        return new_lum
    # end def

    def convert_to_rgb(self) -> np.ndarray:
        hue_to_convert, sat_to_convert, lum_to_convert = self.copy_color()
        rgb_array = np.array(object=colorsys.hls_to_rgb(
            h=hue_to_convert,
            l=lum_to_convert,
            s=sat_to_convert
        ))
        for hue in range(len(rgb_array)):
            rgb_array[hue] = int(round(number=rgb_array[hue] * 255, ndigits=0))
        # end for
        return rgb_array
    # end def
    
# end class