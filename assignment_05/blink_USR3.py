# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink the USR3 LED / blink_USR3.py
--------------------------------------------------------------------------
License:
Copyright 2019 Jason Dennis

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Program that will use the Adafruit library to blink the USR3 LED at 5 Hz

--------------------------------------------------------------------------
"""
import Adafruit_BBIO.GPIO as GPIO
import time
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------


# this type of construct is useful bc sometimes you want to import code; when you
# import code, your "name" changes since it is not the main script

if __name__ == "__main__":
    GPIO.setup("USR3", GPIO.OUT)

    #will cycle through High and Low with a 5 Hz frequency
    while True:

       #sets USR3 LED to high for .1 seconds
        GPIO.output("USR3", GPIO.HIGH)
        time.sleep(.1)

        #sets USR3 LED to low for .1 seconds
        GPIO.output("USR3", GPIO.LOW)
        time.sleep(.1)



