def maxArea(height) -> int:
    most_area = 0
    left_pointer = 0
    right_pointer = len(height) - 1


    while left_pointer < right_pointer:
        area = min(height[left_pointer], height [right_pointer]) * (right_pointer - left_pointer)
        most_area = max(most_area, area)

        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return most_area