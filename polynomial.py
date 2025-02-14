# The poly tool returns the coefficients of a polynomial with the given sequence of roots.
# The roots tool returns the roots of a polynomial with the given coefficients.
# The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
# The polyder tool returns the derivative of the specified order of a polynomial.
# The polyval tool evaluates the polynomial at specific value.
# The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.


# The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, 
# multiplication, and division of polynomial coefficients, respectively.

# Task
# You are given the coefficients of a polynomial P.
# Your task is to find the value of P at point x.

# Input Format
# The first line contains the space separated value of the coefficients in P.
# The second line contains the value of x.

# Output Format
# Print the desired value.

import numpy as np

num = list(map(float, input().split()))

x = float(input())

result = np.polyval(num,  x)
print(result)

