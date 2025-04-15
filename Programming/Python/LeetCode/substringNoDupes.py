def lengthOfLongestSubstring(s: str) -> int:
    result = 0
    last_index = {} # dictionary to store indeces of visited chars

    # Start of current window
    start = 0

    # Move end of current window
    for end in range(len(s)):

        if s[end] in last_index:
            # Starting point = max of either current start or index after last occurence of char
            start = max(start, last_index[s[end]] + 1)

        # Update result if larger window
        result = max(result, end - start + 1)

        # Update last index of s[end]
        last_index[s[end]] = end

    return result

word = " "
print(len(word))
print(lengthOfLongestSubstring(word))