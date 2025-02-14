# The DOT tool returns the dot product of two arrays

# The CROSS tool returns the CROSS product of two arrays

# Task 
# you are given 2 arrays A and B. Both have dimensions of N x N.
# Task is to compute their matrix product.

# Input Format
# The first line contains the integer N.
# The next N lines contains N space separated integers of array A.
# The following N lines contains N space separated integers of array B.

import numpy as np

n = int(input())
A = np.array([list(map(int,input().split())) for _ in range(n)])
B = np.array([list(map(int,input().split())) for _ in range(n)])
print(np.dot(A,B))

# sample input
# 2
# 1 2
# 3 4
# 1 2
# 3 4

# Sample Output
# [[7 10] 
# [15 22]]