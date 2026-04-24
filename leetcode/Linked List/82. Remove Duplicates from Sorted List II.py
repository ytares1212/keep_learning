# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:

# Input: head = [1,1,1,2,3]
# Output: [2,3]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                # Skip all duplicate nodes
                while current.next and current.val == current.next.val:
                    current = current.next
                # Connect the previous node to the node after the duplicates
                prev.next = current.next
            else:
                # Move the previous pointer only if no duplicates were found
                prev = current
            current = current.next

        return dummy.next