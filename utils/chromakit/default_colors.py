#!/usr/bin/python3


# Normalized as 100% NORM_SAT
NORM_SAT = 1

# Default luminosity is the mid-range and represents no change
LUM_DEFAULT = 127.5
LUM_MIN = 0
LUM_MAX = 256

# Defines the base colors only relative to
# the wavelengths on the electromagnetic spectrum.
# Vectors are represented as HSL values with
# where only hue and luminosity are variables
# H is as normalized degrees (degree/360), 
# S and L are normalized %
VISIBLE_LIGHT: dict[str, list] = {
    'DARK_RED_DEFAULT': [0, NORM_SAT, 0.19],      # 780nm
    'RED_DEFAULT': [0, NORM_SAT, 0.50],           # 650nm
    'ORANGE_DEFAULT': [0.0889, NORM_SAT, 0.50],   # 615nm
    'YELLOW_DEFAULT': [0.1556, NORM_SAT, 0.50],   # 585nm
    'GREEN_DEFAULT': [0.2611, NORM_SAT, 0.50],    # 535nm
    'AQUA_DEFAULT': [0.5417, NORM_SAT, 0.50],     # 475nm
    'BLUE_DEFAULT': [0.6028, NORM_SAT, 0.50],     # 455nm
    'INDIGO_DEFAULT': [0.7639, NORM_SAT, 0.429],  # 410nm
    'VIOLET_DEFAULT': [0.7861, NORM_SAT, 0.355]   # 400nm
}

# Defines the greyscale for the color dataset
# in RGB uint8 values
LUMINOSITY_VALUES: dict[str, int] = {
    'DARK_GREY_1': 20, 
    'DARK_GREY_2': 40, 
    'DARK_GREY_3': 60,
    'MED_GREY_1': 80, 
    'MED_GREY_2': 100, 
    'MED_GREY_3': 120,
    'LIGHT_GREY_1': 140, 
    'LIGHT_GREY_2': 160, 
    'LIGHT_GREY_3': 180,
    'VERY_LIGHT_GREY_1': 200, 
    'VERY_LIGHT_GREY_2': 220,
    'VERY_LIGHT_GREY_3': 240
}
