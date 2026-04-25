# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Compute the length of the list and get the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Connect the tail to the head to make it circular
        tail.next = head

        # Find the new tail: (length - k % length - 1)th node
        # and the new head: (length - k % length)th node
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head