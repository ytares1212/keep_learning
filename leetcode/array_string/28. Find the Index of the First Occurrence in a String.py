# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1
        index = 0
        start = 0
        while start <= m - n:
            end = start
            for i in range(n):
                if haystack[end] == needle[i]:
                    end += 1
                    #print(end)
                    if end - start == n:
                        return start
                else:
                    start += 1
                    break
            
        return -1