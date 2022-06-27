# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Optimised solution without recursive programming:
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]


# Brute force version O(k.N)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) > 2 :
            B = self.mergeKLists(lists[1:])
        elif len(lists) == 0:
            return None
        elif len(lists) < 2:
            return lists[0]
        else:
            B = lists[1]

        return self.mergeTwoLists(lists[0], B)



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