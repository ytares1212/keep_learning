# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Example 1:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
# Input: root = []
# Output: []

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the root node. There are no next pointers that need to be set up on the first level
        leftmost = root

        while leftmost:
            # Iterate the "linked list" starting from the head node and using the next pointers, 
            # establish the corresponding links for the next level.
            head = leftmost
            prev = None
            leftmost = None

            while head:
                # Left child
                if head.left:
                    if prev:
                        prev.next = head.left
                    else:
                        leftmost = head.left
                    prev = head.left
                
                # Right child
                if head.right:
                    if prev:
                        prev.next = head.right
                    else:
                        leftmost = head.right
                    prev = head.right
                
                # Move to the next node in the current level
                head = head.next
        
        return root