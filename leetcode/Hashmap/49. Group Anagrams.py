# Given an array of strings strs, group the together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

#     There is no string in strs that can be rearranged to form "bat".
#     The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#     The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      from collections import defaultdict
      mapping = defaultdict(list)
      for s in strs:
        key = ''.join(sorted(s))
        mapping[key].append(s)
      return list(mapping.values())


strs = ["eat","tea","tan","ate","nat","bat"]
a = Solution.groupAnagrams('', strs)
print(a)