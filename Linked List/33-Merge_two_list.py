# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# the trick here is to think as a pointer on a list.
# We thus create 2 pointers, one at the front of ourlist, that will thusd be returned
# Onefrom whihc we will increment the nodes 1 by 1

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = ListNode()
        tail = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return merged_list.next