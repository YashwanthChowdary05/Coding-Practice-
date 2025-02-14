# ABC is a right triangle, 90 at B.
# Therefore, ABC = 90.

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find MBC (angle , as shown in the figure) in degrees.

# Input Format
# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Constraints
# 0 <= AB <= 100
# 0 <= BC <= 100 
# Lengths AB and BC are natural numbers.

# Output Format
# Output MBC in degrees.
# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.4999999°, then output 56°.


import math 

opp = int(input()) 
adj = int(input())

hypotenuse = opp/adj 
tan_value = math.atan(hypotenuse) 
degree = math.degrees(tan_value)

angle = round(degree) 
e = chr(176) 
print(f"{angle}{e}")


# Sample Input 
# 10
# 10