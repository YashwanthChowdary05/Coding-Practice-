# The inner tool returns the inner product of two arrays.
# The outer tool returns the outer product of two arrays.

# Task
# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.

# Input Format
# The first line contains the space separated elements of array A.
# The second line contains the space separated elements of array B.

# Output Format
# First, print the inner product.
# Second, print the outer product.

import numpy as np

A = np.array(list(map(int,input().split)))
B = np.array(list(map(int,input().split)))
print(np.inner(A,B))
print(np.outer(A,B))

# Sample Input
# 0 1
# 2 3

# Sample Output
# 3
# [[0 0] 
#  [2 3]]