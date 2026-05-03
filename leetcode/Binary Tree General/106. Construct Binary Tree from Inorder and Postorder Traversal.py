# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Example 1:

# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        # root.left = self.buildTree(inorder[:root_index], postorder[])
        # root.right = self.buildTree(inorder[root_index + 1:], postorder[])
        # The left subtree will be built from the first root_index elements of the inorder list and the 
        # first root_index elements of the postorder list.
        # The right subtree will be built from the elements after root_index in the inorder list and the 
        # elements after root_index in the postorder list, excluding the last element which is the root.
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])

        return root