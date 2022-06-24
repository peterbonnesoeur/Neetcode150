# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# Simply fill a list of the nodes and
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_node = []
        tail = head

        while tail is not None:
            list_node.append(tail)
            tail = tail.next

        list_node.append(None)


        index = len(list_node) - n - 1

        if index - 1 < 0:
            return head.next

        list_node[index - 1].next = list_node[index + 1]

        return head