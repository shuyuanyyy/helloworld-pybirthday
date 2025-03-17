"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import pybirthday


def main():
    """
    Get some birthday-themed visuals.
    """
    line = pybirthday.cake('Alex', 'Words')
    print(line)

    candle_str = pybirthday.candle(3)
    print(candle_str)

if __name__ == "__main__":
    # run the main function
    main()