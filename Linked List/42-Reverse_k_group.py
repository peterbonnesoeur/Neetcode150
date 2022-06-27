# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# More succinct solution where we already go through the list and reverse the nodes
# without any mini_lists
class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

# 3 steps :
# 1 - create min linked lists
# 2 -reverse the last slots in case taht it is not complete
# 3 - merge the linked lists
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        mini_lists = []


        currentNode, previousNode = head, None
        count = 0

        # Generate some minilists for all the mini-inversed linked lists
        while currentNode is not None:
            temp = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = temp
            count += 1
            if count == k:
                count = 0
                mini_lists.append((previousNode, head))
                head = currentNode
                previousNode = None

        # In case a mini linked list is not of the desired size, reinverse it
        if previousNode is not None:
            head = previousNode
            currentNode, previousNode = head, None
            while currentNode is not None:
                temp = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = temp

            mini_lists.append((previousNode, head))

        # Link the mini linked lists together
        new_head = mini_lists[0][0]
        previousNode = mini_lists[0][1]
        for (min_prev, min_head) in mini_lists[1:]:
            previousNode.next = min_prev
            previousNode = min_head


        return new_head


