# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Simple Calculator / simple_calc.py
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

Simple calculator that will do +, -, *, / and pow

- Take in two numbers
- Take in an operator
- Perform Calculation and output
- Repeat

Error conditions:
- invalid calculation
- invalid number inputs
- invalid operator

--> results in error message and exists the program
--------------------------------------------------------------------------
"""

import operator
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
operators = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "<<" : operator.lshift,
    ">>" : operator.rshift,
    "%" : operator.mod,
    "**" : operator.pow
}

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------
def get_user_input():
    """ Will return (num1, num2, operator) or (None, None, None) on error"""
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        op = input("Enter an operator like 'operator' (valid operators are +,-,*,/, <<, >>, %, and **): ")

        return(number1, number2,op)
    except Exception as e:
        print(e)
        print("Invalid input!")
        return (None, None, None)

# End def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------


# this type of construct is useful bc sometimes you want to import code; when you
# import code, your "name" changes since it is not the main script

if __name__ == "__main__":
    try:
        input = raw_input
    except NameError:
        pass

    while True:
        (number1, number2, op) = get_user_input()

        func = operators.get(op, None)


        if (number1 is None) or (number2 is None) or (func is None):
            print("Program Exiting")
            break
        else:
            #do the math

            # pass in key and this will return value
            # func = operators.get(op, None)

            print(func(number1, number2))


