# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
#     For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.

# Example 1:
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

# Example 2:
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        s = set(bank)
        if endGene not in s and startGene != endGene:
            return -1
        q = deque([(startGene, 0)])
        v = {startGene}
        while q:
            g, d = q.popleft()
            if g == endGene:
                return d
            for i in range(8):
                for c in 'ACGT':
                    if g[i] != c:
                        n = g[:i] + c + g[i+1:]
                        if n in s and n not in v:
                            v.add(n)
                            q.append((n, d+1))
        return -1