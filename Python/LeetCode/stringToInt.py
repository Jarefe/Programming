def myAtoi(s:str) -> int:
    trimmed = s.strip()
    integer = 0
    placeholder = []
    number_read = False

    for char in trimmed:

        if char == '+' and not number_read:
            placeholder.append(char)
            continue
        elif char == '-' and not number_read:
            placeholder.append(char)
            continue
        elif char.isdigit():
            placeholder.append(char)
            number_read = True
        else:
            break

    


    if not placeholder:
        return 0

    try:
        integer = int(''.join(placeholder))
    except:
        return 0

    if integer < -2**31:
        return -2**31
    
    if integer > 2**31 - 1:
        return 2**31 - 1

    return integer
