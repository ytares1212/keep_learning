# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 6

# Example 2:

# Input: root = []
# Output: 0

# Example 3:

# Input: root = [1]
# Output: 1
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = root
        right = root
        left_h = 0
        right_h = 0

        while left:
            left_h += 1
            left = left.left
        while right:
            right_h += 1
            right = right.right
        
        if left_h == right_h:
            return (1 << left_h) - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1