# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

#     For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
      # detailed explanation:
      # 1. We first check if the input string s or the list of words is empty. If either is empty, we return an empty list since there can be no concatenated substrings.
      # 2. We calculate the length of each word (assuming all words are of the same length) and the total length of the concatenated string we are looking for (which is the length of one word multiplied by the number of words).
      # 3. We create a frequency dictionary (word_freq) to count how many times each word appears in the list of words.
        res = []
        word_freq = {}
        n = len(s)
        word_size = len(words[0])
        num_of_words = len(words)
        premu_len = word_size * num_of_words
        last_possible_start = n - premu_len + 1
        if n < premu_len:
            return []
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        #print(word_freq)
        for start in range(last_possible_start):
            seen_word = {}
            for jump in range(num_of_words):
                curr_word_start = start + jump * word_size
                curr_word_end = curr_word_start + word_size
                curr_word = s[curr_word_start:curr_word_end]

                if curr_word in words:
                    seen_word[curr_word] = seen_word.get(curr_word, 0) + 1

                    if seen_word[curr_word] > word_freq[curr_word]:
                        break
                else:
                    break
            # why here a else without if?
            # The else block is associated with the inner for loop, not the if statement. In Python, a for loop can have an else block that executes only if the loop completes 
            # without encountering a break statement. In this case, if we successfully find all the words in the current substring without breaking out of the loop, 
            # we append the starting index i to the result list. If we encounter a break (either because a word is not in word_freq or because we have seen a word too many times), 
            # the else block will not execute, and we will move on to the next starting index.
            else:
                res.append(start)
                

        return res