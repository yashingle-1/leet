from P2.add2num import ListNode
class Solution:
    def sortList(self, head):
        
        # If list is empty OR has only one node, it is already sorted
        if not head or not head.next:
            return head

        # Initialize slow and fast pointers to find middle of list
        slow, fast = head, head.next
        
        # Move fast pointer twice as fast as slow pointer
        # When fast reaches end, slow will be at middle
        while fast and fast.next:
            slow = slow.next          # Move slow by 1 step
            fast = fast.next.next     # Move fast by 2 steps

        # mid will be start of second half
        mid = slow.next
        
        # Break the list into two halves
        slow.next = None

        # Recursively sort left half
        left = self.sortList(head)

        # Recursively sort right half
        right = self.sortList(mid)

        # Merge two sorted halves and return result
        return self.merge(left, right)


    def merge(self, l1, l2):
        
        # Create dummy node to simplify merging
        dummy = ListNode(0)
        
        # curr pointer helps build merged list
        curr = dummy

        # Compare nodes of both lists until one finishes
        while l1 and l2:
            
            # If left list value is smaller
            if l1.val < l2.val:
                curr.next = l1      # Attach l1 node to merged list
                l1 = l1.next        # Move l1 forward
            
            else:
                curr.next = l2      # Attach l2 node
                l2 = l2.next        # Move l2 forward
            
            curr = curr.next        # Move merged list pointer forward

        # If any nodes left in either list, attach them
        curr.next = l1 or l2

        # dummy.next is actual start of merged sorted list
        return dummy.next