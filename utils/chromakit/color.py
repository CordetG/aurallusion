#!/usr/bin/python3

class Color:
    '''Manage the color values and calculations using both
    the visible light spectrum and luminosity to create colors.
    -----------
    Attributes:
        hue -- Normalized hue of degree value
        sat -- Normalized saturation of a percent value
        lum -- Normalized Brightness of a percent value
    '''

    def __init__(self, color: list) -> None:
        self.hue = color[0]
        self.sat = color[1]
        self.lum = color[2]
    # end __init__ def
    
# end class