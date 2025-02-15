# You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether
# his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

# A valid credit card from ABCD Bank has the following characteristics:

# ► It must start with a 4, 5 or 6.
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits.

# Input Format:
# The first line of input contains an integer N.
# The next N lines contain credit card numbers.

# Constraints
# 0 < N < 100

# Output Format
# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

import re 

check1 = r'(?=(.)(-?\1){3,}.*)'
validcredit = r'^(4|5|6)[0-9]{3}(-?[0-9]{4}){3}$'

check1 = re.compile(check1)
check2 = re.compile(validcredit)

t = int(input())

for i in range(t):
    num = input()
    if check1.search(num):
        print("Invalid")
    elif check2.match(num):
        print("Valid")
    else:
        print("Invalid")