# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        mp = defaultdict(list)
        leng = len(nums)
        for i in range(leng):
            mp[nums[i]].append(i)

            if len(mp[nums[i]]) == 2:
                if abs(mp[nums[i]][0] - mp[nums[i]][1]) <= k:
                    return True
                else:
                    mp[nums[i]].pop(0)
        return False

        # seen = {}

        # for i, val in enumerate(nums):
        #     if val in seen and i - seen[val] <= k:
        #         return True
        #     else:
        #         seen[val] = i
        
        # return False