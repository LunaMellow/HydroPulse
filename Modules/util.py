"""

    Utility Module
    --------------
    Contains general utility functions used across the application for mathematical calculations, randomization, etc.

"""


# Function for linear interpolation
def lerp(start, end, t):
    return start + (end - start) * t
