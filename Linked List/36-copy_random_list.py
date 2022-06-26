"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#The trick is to use a dictionnary that wil hold the nodes to
# draw back their relationships (this is a bit meh in case 2 nodes have the same value)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = {None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            copy_dict[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copy_dict[curr]
            copy.next = copy_dict[curr.next]
            copy.random = copy_dict[curr.random]
            curr = curr.next

        return copy_dict[head]


# Brute force solution:

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = {None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            copy_dict[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copy_dict[curr]
            copy.next = copy_dict[curr.next]
            copy.random = copy_dict[curr.random]
            curr = curr.next

        return copy_dict[head]



    def copyRandomList_(self, head: 'Optional[Node]') -> 'Optional[Node]':
        my_copy_head =my_copy =  None

        tail = head
        length_linked_list = 0

        while tail:
            if not my_copy:
                my_copy = Node(tail.val)
                my_copy_head = my_copy
            else:
                my_copy.next = Node(tail.val)
                my_copy = my_copy.next

            my_copy.random = None

            tail = tail.next
            length_linked_list += 1

        current_node = my_copy_head

        while head:
            random_pointer = head.random
            count = 0
            while random_pointer:
                random_pointer = random_pointer.next
                count += 1

            if count > 0:
                current_node.random = my_copy_head
                for i in range(length_linked_list - count ):
                    current_node.random = current_node.random.next

            head = head.next
            current_node = current_node.next

        return my_copy_head