#!/usr/bin/python3

from .color import *
from .default_colors import *
import numpy as np

class ColorPalette:
    '''Create an array of colors.
    -----------
    Attributes:
        colors -- list of colors represented as (r,g,b) values
    '''
    
    def __init__(self) -> None:
        self.colors: list[int] = []
    # end __init__ def

    def add_base_colors(self) -> np.ndarray:
        for base_color in VISIBLE_LIGHT:
            color_to_add = Color(color=VISIBLE_LIGHT[base_color])
            rgb_vector = color_to_add.create_color().tolist()
            self.colors.append(rgb_vector)
        # end for
        return self.copy_color_vectors()
    # end def

    def add_greyscale(self) -> np.ndarray:
        for grey_val in LUMINOSITY_VALUES:
            grey_vector = np.full(shape=3, fill_value=round(
                number=(LUMINOSITY_VALUES[grey_val]), ndigits=3))
            self.colors.append(grey_vector.tolist())
        # end for
        return self.copy_color_vectors()
    # end def

    def add_scaled_colors(
            self,
            uint8_greyscales: np.ndarray,
            color_to_scale: list
        ) -> np.ndarray:
        for scale in uint8_greyscales:
            color_to_mix = Color(color=color_to_scale)
            rgb_vector = color_to_mix.create_color(scaling=scale).tolist()
            self.colors.append(rgb_vector)
        # end for
        return self.copy_color_vectors()
    # end def

    def copy_color_vectors(self) -> np.ndarray:
        src_vector = np.array(object=self.colors)
        new_vector = src_vector.copy()
        return new_vector
    # end def 
# end class