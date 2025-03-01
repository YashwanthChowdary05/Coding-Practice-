# In Python, a string can be split on a delimiter.

# Example:
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']

# Joining a string is simple:
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 
# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Function Description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:

# string line: a string of space-separated words

# Returns:
# string: the resulting string

def split_join(line):
    words = line.split()
    return '-'.join(words)

if __name__ == '__main__':
    line = input()
    result = split_join(line)
    print(result)

# Sample Input:
# Yashw anth Chow dary

# Sample Output:
# Yashw-anth-Chow-dary