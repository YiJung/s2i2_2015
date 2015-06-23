#! /usr/bin/env python

''' This is a python module that converts temperatures. '''

#The following function converts from Farenheit to Kelvin.
def f_to_k(tempi):
    converted = ((tempi - 32.0) * (5.0 / 9.0) + 273.15
    return converted

print(f_to_k(32))
print(f_to_k(100))
