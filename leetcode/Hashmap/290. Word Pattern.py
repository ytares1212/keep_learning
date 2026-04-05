# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

#     Each letter in pattern maps to exactly one unique word in s.
#     Each unique word in s maps to exactly one letter in pattern.
#     No two letters map to the same word, and no two words map to the same letter.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

#     'a' maps to "dog".
#     'b' maps to "cat".

# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        if len(pattern) != len(words):
            return False
        s_map = {}
        p_map = {}
        for i in range(len(pattern)):
            if pattern[i] not in p_map:
                p_map[pattern[i]] = i
            if words[i] not in s_map:
                s_map[words[i]] = i
            if p_map[pattern[i]] != s_map[words[i]]:
                return False
        return True