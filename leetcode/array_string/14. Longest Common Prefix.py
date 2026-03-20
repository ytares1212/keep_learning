# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs)
        if n < 1:
            return ''
        len_list = [len(x) for x in strs]
        m = min(len_list)
        prefix_len = 0
        while prefix_len < m:
            prefix = strs[0][prefix_len]
            for i in range(1, n):
                if strs[i][prefix_len] == prefix:
                    continue
                else:
                    return strs[0][:prefix_len]
                    
            prefix_len += 1
        return strs[0][:prefix_len]