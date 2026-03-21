# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

#     A word is defined as a character sequence consisting of non-space characters only.
#     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#     The input array words contains at least one word.

 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

# my solution
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #words_map = {}
        length = 0
        sentences = []
        temp = []
        res = []
        for word in words:
            length += len(word) + 1
            if length <= maxWidth + 1:
                temp.append(word)
            else:
                length = len(word) + 1
                sentences.append(temp)
                temp = [word]
        sentences.append(temp)
        #print(sentences)
        for i in range(len(sentences) - 1):

            num_of_word = len(sentences[i])
            if num_of_word == 1:
                num_of_space = 1
                space_length = maxWidth - len(sentences[i][0])
                sentence = sentences[i][0] + ' ' * space_length
                res.append(sentence)
                continue
            else:
                num_of_space = num_of_word - 1

            total_length = 0
            for j in range(num_of_word):
                total_length += len(sentences[i][j])
            
            length_for_space = maxWidth - total_length

            if length_for_space % num_of_space == 0:
                space_length = length_for_space // num_of_space
                space_placeholder = [' ' * space_length] * num_of_space
            else:
                extra_space = length_for_space % num_of_space
                space_length = length_for_space // num_of_space
                space_placeholder = [' ' * space_length] * num_of_space
                for k in range(extra_space):
                    space_placeholder[k] += ' '
            
            # sentences = ['This', 'is', 'an']
            # space_placeholder = ['    ', '    ']
            sentence = ''
            for l in range(num_of_space):
                sentence += sentences[i][l]
                sentence += space_placeholder[l]
            sentence += sentences[i][-1]
            res.append(sentence)

        last_sentence = sentences[-1]
        num_of_word = len(last_sentence)
        if num_of_word == 1:
            space_length = maxWidth - len(last_sentence[0])
            senctence = last_sentence[0] + ' ' * space_length
            res.append(senctence)
        else:
            sentence = ''
            for word in last_sentence[:-1]:
                sentence += word + ' '
            sentence += last_sentence[-1]
            last_space = maxWidth - len(sentence)
            sentence += ' ' * last_space
            res.append(sentence)
        return res

# better solution
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        start = 0
        while start < n:
            end = start
            line_len = 0
            while end < n and line_len + len(words[end]) + end - start <= maxWidth:
                line_len += len(words[end])
                end += 1
            if end == n:
                line = ' '.join(words[start:end])
                line += ' ' * (maxWidth - len(line))
                res.append(line)
                break
            space_num = maxWidth - line_len
            if end - start == 1:
                line = words[start] + ' ' * space_num
                res.append(line)
            else:
                avg_space_num = space_num // (end - start - 1)
                extra_space_num = space_num % (end - start - 1)
                line = ''
                for i in range(start, end):
                    line += words[i]
                    if i < end - 1:
                        line += ' ' * avg_space_num
                        if extra_space_num > 0:
                            line += ' '
                            extra_space_num -= 1
                res.append(line)
            start = end
        return res