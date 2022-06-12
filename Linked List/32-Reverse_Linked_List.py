# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode, previousNode = head, None

        while currentNode is not None:
            temp = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = temp

        return previousNode
