# Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
from typing import List
class Solution: 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # We can use the sliding window technique to solve this problem. We will maintain a window of 
        # elements that we will expand and contract as needed. We will keep track of the sum of the 
        # elements in the current window and the minimum length of a valid subarray found so far. 
        # We will expand the window by moving the right pointer to the right until the sum is greater 
        # than or equal to the target. Once we have a valid window, we will contract it by moving the 
        # left pointer to the right until the sum is less than the target. During this process, we will 
        # update the minimum length of a valid subarray found so far.
        n = len(nums)
        left = 0
        curr_sum = 0
        res = float('inf')

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if res == float('inf') else res