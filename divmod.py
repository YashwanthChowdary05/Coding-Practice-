<<<<<<< HEAD
# One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing
# the quotient of a/b first and then the remainder .

# For example:
# >>> print divmod(177,10)
# (17, 7)
# Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

# Task:
# Read in two integers, a and b, and print three lines.
# The first line is the integer division a//b (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: a%b.
# The third line prints the divmod of a and b.

a = int(input())
b = int(input())

print(a//b)
print(a % b)
=======
# One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing
# the quotient of a/b first and then the remainder .

# For example:
# >>> print divmod(177,10)
# (17, 7)
# Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

# Task:
# Read in two integers, a and b, and print three lines.
# The first line is the integer division a//b (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: a%b.
# The third line prints the divmod of a and b.

a = int(input())
b = int(input())

print(a//b)
print(a % b)
>>>>>>> dca8827d2ec7890a76e5ff6732843232ed31823e
print(divmod(a, b))