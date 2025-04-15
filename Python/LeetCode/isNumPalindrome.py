def isPalindrome(x: int) -> bool:
    num_string = str(x)
    num_reversed = num_string[::-1]

    return num_string == num_reversed