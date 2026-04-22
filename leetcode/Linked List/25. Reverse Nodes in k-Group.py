# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            kth_node = prev_group_end
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            group_start = prev_group_end.next
            next_group_start = kth_node.next

            # Reverse the current group
            prev, current = None, group_start
            while current != next_group_start:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            # Connect the previous group with the reversed group
            prev_group_end.next = kth_node
            group_start.next = next_group_start

            # Move to the end of the reversed group for the next iteration
            prev_group_end = group_start
        