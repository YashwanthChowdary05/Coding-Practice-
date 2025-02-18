<<<<<<< HEAD
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:
# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(1,int(input())+1):
=======
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:
# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(1,int(input())+1):
>>>>>>> dca8827d2ec7890a76e5ff6732843232ed31823e
    print (((10**i - 1)//9)**2) 