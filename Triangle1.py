<<<<<<< HEAD
# You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:

# 1
# 22
# 333
# 4444
# 55555
# Can you do it using only arithmetic operations, a single for loop and print statement?

# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

# Note: Using anything related to strings will give a score of 0.

# Input Format
# A single line containing integer, N.

# Output Format
# Print N-1 lines as explained above.

# Input: Positive integer N
N = int(input("Enter a positive integer N: "))

# Loop through rows from 1 to N-1
for i in range(1, N):
=======
# You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:

# 1
# 22
# 333
# 4444
# 55555
# Can you do it using only arithmetic operations, a single for loop and print statement?

# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

# Note: Using anything related to strings will give a score of 0.

# Input Format
# A single line containing integer, N.

# Output Format
# Print N-1 lines as explained above.

# Input: Positive integer N
N = int(input("Enter a positive integer N: "))

# Loop through rows from 1 to N-1
for i in range(1, N):
>>>>>>> dca8827d2ec7890a76e5ff6732843232ed31823e
    print(str(i) * i)