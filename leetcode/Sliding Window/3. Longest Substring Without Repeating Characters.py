# Given a string s, find the length of the longest without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = left = 0
        n = len(s)
        str_set = set()
        for right in range(n):

            while s[right] in str_set:
                str_set.remove(s[left])
                left += 1
            str_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len