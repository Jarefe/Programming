def zigzagConversion(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    zigzagArray = ['']*numRows
    index = 1
    up = True

    # Loop maps characters by which row theyre in then concatenates them per row
    # i.e. PAYPALISHIRING,3 -> [PAHN,APLSIIG,YIR]
    for char in s:
        zigzagArray[index-1] += char
        if index == numRows:
            up = False
        elif index == 1:
            up = True

        if up:
            index += 1
        else:
            index -= 1
        


    return "".join(zigzagArray)
        
zigzagConversion("PAYPALISHIRING", 3)