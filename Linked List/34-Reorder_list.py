# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next






# Too slow application - work in progress
# The trick here is to do a recursive app
# The issue behing is that we do not remember about the previous element
# Here, the issue is that we are going through the list oer and over and over again O(n!)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """


        while head:
            tail = head
            count = 0
            while tail.next is not None:
                next_ = tail.next
                if next_.next is None:
                    tail.next = None
                tail = next_
                count += 1

            temp = head.next
            head.next = tail
            tail.next = temp


            if count > 3:
                head = head.next.next
            else:
                head = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # the idea here is to use a slow and fast pointer to reach the
        # middle andend of the sorted list O(N)
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_fast = slow.next
        slow.next = prev = None

        # THen, we inverse the sorted list O(N/2)
        while head_fast:
            tmp = head_fast.next
            head_fast.next = prev
            prev = head_fast
            head_fast = tmp

        first, second = head, prev

        # Finally, wetraverse thelist while intercaling
        # the values of both lists O(N/2)
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2