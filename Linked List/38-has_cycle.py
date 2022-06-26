# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Really efficient: Tortoise and hair method:

# if there is a loop, at a given moment, fast will catch up on slow
# if this is not the case, meaning the linked list is finite, then we will reach a value of none
# for fast and reach an exception
class Solution:
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

# We just use a set to see if a node was already visited.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_nodes = set()
        curr = head

        while curr:
            if curr not in set_nodes:
                set_nodes.add(curr)
            else:
                return True
            curr = curr.next


        return False
