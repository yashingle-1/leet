# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return the head of the merged sorted list.

        Args:
            list1: Head of the first sorted linked list
            list2: Head of the second sorted linked list

        Returns:
            Head of the merged sorted linked list
        """
        # Base case: if either list is empty, return the other list
        if list1 is None or list2 is None:
            return list1 or list2

        # Compare the values of the current nodes
        if list1.val <= list2.val:
            # If list1's value is smaller or equal, use list1's node
            # Recursively merge the rest of list1 with list2
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # If list2's value is smaller, use list2's node
            # Recursively merge list1 with the rest of list2
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2