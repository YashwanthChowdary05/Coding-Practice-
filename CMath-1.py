# Task:
# You are given a complex . Your task is to convert it to polar coordinates.

# Input Format:
# A single line containing the complex number . Note: complex() function can be used in 
# python to convert the input as a complex number.

# Constraints:
# Given number is a valid complex number

# Output Format
# Output two lines:
# The first line should contain the value of R.
# The second line should contain the value of gamma.


import cmath

def r_phase(n=complex(input())): 

    print(f'{cmath.polar(n)[0]}\n{cmath.polar(n)[1]}')

r_phase()

# Sample Input:
# 1+2j

# Smaple Output
# 2.23606797749979
# 1.1071487177940904
