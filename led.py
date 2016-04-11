"""
This module allows the color of a common anode LED to be set by name: RED,
GREEN or BLUE.

For pin numbering on the Raspberry Pi, see:
https://www.raspberrypi.org/documentation/usage/gpio/
"""

import RPi.GPIO as GPIO
import atexit

PINS = [15, 13, 11] # red, green, blue

colors = {
    'RED': (1,0,0),
    'GREEN': (0,1,0),
    'BLUE': (0,0,1),
    None: (0,0,0),
}

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    for PIN in PINS:
        GPIO.setup(PIN, GPIO.OUT)
setup()

def set_color(name):
    """Set the color of the LED"""
    rgb = colors[name]
    for PIN, val in zip(PINS, rgb):
        GPIO.output(PIN, [GPIO.HIGH, GPIO.LOW][val])

# ensure the LED is turned off when the program exits
atexit.register(lambda: set_color(None))
