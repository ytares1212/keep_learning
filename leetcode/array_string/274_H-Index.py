from typing import List

# Given an array of integers citations where citations[i] is the number of citations a researcher received for 
# their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such 
# that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 
# citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 
# citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1

# Constraints:
#     n == citations.length
#     1 <= n <= 5000
#     0 <= citations[i] <= 1000

class Solution:
    def hIndex(self, citations: List[int]) -> int:
      
      # my solution
      # citations.sort(reverse=True)
      # n = len(citations)
      # # iterate from the maximum possible h-index (which is the number of papers) down to 0
      # while n > 0:
      #     max_h = 0
      #     # count how many papers have at least n citations
      #     for i in range(n):
      #         if citations[i] >= n:
      #             max_h += 1
      #     # if the count of papers with at least n citations is less than n, decrease n and check again
      #     if max_h != n:
      #         n -= 1
      #     else:
      #         return max_h
      # return 0
      
      # optimal solution using counting sort
      papers = len(citations)
      citation_buckets = [0] * (papers + 1)
      # count how many papers have a certain number of citations, but cap the count at the total number of papers
      for citation in citations:
          citation_buckets[min(citation, papers)] += 1
      
      cumulative_papers = 0
      # iterate from the maximum possible h-index (which is the number of papers) down to 0
      for h_index in range(papers, -1, -1):
          # keep a running total of how many papers have at least h_index citations
          # cumulative_papers will represent the total number of papers that have at least h_index citations
          cumulative_papers += citation_buckets[h_index]
          if cumulative_papers >= h_index:
              return h_index


        