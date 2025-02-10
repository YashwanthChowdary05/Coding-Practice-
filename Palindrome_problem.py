# Check given number is palindrome or not

def is_number_palindrome(n: int) -> bool:
    str_n = str(n)
    
    return str_n == str_n[::-1]

print(is_number_palindrome(121))
print(is_number_palindrome(176))
print(is_number_palindrome(0))
