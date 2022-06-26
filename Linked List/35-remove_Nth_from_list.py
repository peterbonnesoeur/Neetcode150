# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Better approach
# First, we do not need to know the total length of the
# linked list to remove the n_th element. Once we go through more
# than n elements, we can start incrementing a pointer from the head of
# the linked list.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        tail = head
        n_node = head

        count = 0
        while tail:
            tail = tail.next
            if count > n:
                n_node = n_node.next
            count += 1

        if count == n:
            return head.next

        temp = n_node.next
        n_node.next = temp.next

        return head



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