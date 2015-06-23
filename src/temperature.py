#! /usr/bin/env python

''' This is a python module that converts temperatures. '''

#The following function converts from Farenheit to Kelvin.
def f_to_k(tempi):
    converted = ((tempi - 32.0) * (5.0 / 9.0)) + 273.15
    return converted

def k_to_c(tempi):
    return tempi - 273.15

def f_to_c(tempi):
    temp_k = f_to_k(tempi)
    result = k_to_c(temp_k)
    return result

print(f_to_k(32))
print(f_to_k(100))
print(k_to_c(273.15))
print(f_to_c(32))
