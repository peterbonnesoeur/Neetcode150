# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This is a basic addition in this case.
# The trick is to consider a carry and iterate on l1 and l2
# if they still exist. We then build the listnode iteratively.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        buffer = 0

        while l1 or l2 or buffer:
            val = buffer
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            buffer = val // 10
            val %= 10

            if head:
                curr.next = ListNode(val)
                curr = curr.next
            else:
                head = ListNode(val)
                curr = head

        return head