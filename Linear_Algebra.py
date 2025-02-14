# The NumPy module also comes with a number of built-in routines for linear algebra calculations. 
# These can be found in the sub-module linalg.

# The linalg.det tool computes the determinant of an array.
# The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
# The linalg.inv tool computes the (multiplicative) inverse of a matrix.

# Task:
# You are given a square matrix A with dimensions N x N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

# Input Format

# The first line contains the integer N.
# The next N lines contains the N space separated elements of array A.

# Output Format
# Print the determinant of A.

import numpy as np
n = int(input())

a = np.array([list(map(float,input().split(" "))) for _ in range(n)])
print(round(np.linalg.det(a),2))

# Sample Input
# 2
# 1.1 1.1
# 1.1 1.1