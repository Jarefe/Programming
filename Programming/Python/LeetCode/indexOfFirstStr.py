def strStr(haystack: str, needle: str) -> int:
    return haystack.index(needle) if needle in haystack else -1

haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack, needle))