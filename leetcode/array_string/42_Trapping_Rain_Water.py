# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # We can use two pointers to solve this problem. We will maintain two pointers, 
        # one at the beginning of the array and one at the end. We will also keep track of the 
        # maximum height seen so far from both ends.
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0
        # We will move the pointers towards each other, and at each step, we will calculate the 
        # trapped water based on the maximum height seen so far from both ends. 
        # If the left maximum is less than the right maximum, we will move the left pointer and 
        # update the left maximum. Otherwise, we will move the right pointer and update the right 
        # maximum. We will continue this process until the two pointers meet.
        while left < right:
            # If the left maximum is less than the right maximum, we can calculate the trapped water 
            # at the left pointer and move it to the right. Otherwise, we can calculate the trapped 
            # water at the right pointer and move it to the left.
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped_water += max(0, left_max - height[left])

            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += max(0, right_max - height[right])

        return trapped_water
