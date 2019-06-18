#!/usr/bin/env python
#
# https://www.dexterindustries.com
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md
#
# This code is for power management on a Raspberry Pi with GoPiGo3.
#
# GPIO 22 will be configured as input with pulldown. If pulled high, the RPi will halt.
#
# GPIO 23 needs to remain low impedance (output) set to a HIGH state. If GPIO 23 gets
# left floating (high impedance) the GoPiGo3 assumes the RPi has shut down fully.
# SW should never write GPIO 23 to LOW or set it as an INPUT.


import RPi.GPIO as GPIO
import time
import os

# use BCM numbering
GPIO.setmode(GPIO.BCM)

# Make sure GPIO 18 stays high, to prevent floating low and resetting the GPG3
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)

# Set power signal line from GPG3 as input with pulldown
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set power signal line to GPG3 as output high
GPIO.setup(23, GPIO.OUT, initial=GPIO.HIGH)

while True:
    # Shutdown at the request of the GPG3
    if GPIO.input(22):
        os.system("shutdown now -h")
    time.sleep(0.1)
