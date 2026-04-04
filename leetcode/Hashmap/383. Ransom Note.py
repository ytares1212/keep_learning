# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# use hashmap to count the frequency of each character in magazine, then check if the frequency of each character in ransomNote is less than 
# or equal to the frequency in magazine
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        magazine_count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)

        for char, count in ransomNote_count.items():
            if magazine_count[char] < count:
                return False
        return True