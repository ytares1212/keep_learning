  # Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

  # Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

  # The tests are generated such that there is exactly one solution. You may not use the same element twice.

  # Your solution must use only constant extra space.

  

  # Example 1:

  # Input: numbers = [2,7,11,15], target = 9
  # Output: [1,2]
  # Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

  # Example 2:

  # Input: numbers = [2,3,4], target = 6
  # Output: [1,3]
  # Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

  # Example 3:

  # Input: numbers = [-1,0], target = -1
  # Output: [1,2]
  # Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum_ = numbers[left] + numbers[right]

            if sum_ == target:
                return [left + 1, right + 1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
# why list index out of range
# the problem is that the input array is 1-indexed, but in Python, list indices are 0-indexed. So when we return the indices, we need to add 1 to each index to convert them from 0-indexed to 1-indexed.
# For example, if the two numbers that add up to the target are at indices 0 and 1 in the 0-indexed array, we need to return [1, 2] instead of [0, 1] to match the 1-indexed requirement of the problem.