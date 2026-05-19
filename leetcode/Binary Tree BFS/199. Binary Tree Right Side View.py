# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 4:
# Input: root = []
# Output: []

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i == 0:
                    res.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res