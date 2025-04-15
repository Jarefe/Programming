def reverse(x: int) -> int:
    negative = "-"
    num_str = ""

    if x < 0:
        x = x * -1
        num_str = str(x)
        reversed_str = negative + num_str[::-1]
    else:
        num_str = str(x)
        reversed_str = num_str[::-1]

    reversed_num = int(reversed_str)

    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num

print(reverse(-123))