# Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # We can use the sliding window technique to solve this problem. We will maintain a window of 
        # characters that we will expand and contract as needed. We will keep track of the frequency of 
        # characters in the current window and the frequency of characters in t. We will expand the 
        # window by moving the right pointer to the right until we have a valid window that contains all 
        # characters in t. Once we have a valid window, we will contract it by moving the left pointer to 
        # the right until we no longer have a valid window. During this process, we will update the 
        # minimum length of a valid window found so far and the starting index of that window.
        from collections import Counter
        t_freq = Counter(t)
        window_freq = {}
        have, need = 0, len(t_freq)
        res = [float('inf'), None]
        left = 0

        for right in range(len(s)):
            c = s[right]
            window_freq[c] = 1 + window_freq.get(c, 0)

            if c in t_freq and window_freq[c] == t_freq[c]:
                have += 1

            while have == need:
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left]

                window_freq[s[left]] -= 1
                if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1

        return "" if res[0] == float('inf') else s[res[1]:res[1] + res[0]]