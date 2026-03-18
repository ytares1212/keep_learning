# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        roman = { 'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        for i in range(n - 1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        res += roman[s[-1]]
        return res
        # for i in range(n - 1):
        #     if s[i] == 'I':
                
        #         if s[i+1] == 'V' or s[i+1] == 'X':
        #             res -= 1
        #         else:
        #             res += 1
        #         continue
        #     if s[i] == 'V':
        #         res += 5
        #         continue
        #     if s[i] == 'X':
        #         if s[i+1] == 'L' or s[i+1] == 'C':
        #             res -= 10
        #         else:
        #             res += 10
        #         continue
        #     if s[i] == 'L':
        #         res += 50
        #         continue
        #     if s[i] == 'C':
        #         if s[i+1] == 'D' or s[i+1] == 'M':
        #             res -= 100
        #         else:
        #             res += 100
        #         continue
        #     if s[i] == 'D':
        #         res += 500
        #         continue
        #     if s[i] == 'M':
        #         res += 1000
        #         continue

        #     print(res)
        # res += num[s[-1]]
        # return res
