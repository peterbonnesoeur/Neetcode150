
#Real tricky one
# First, we need to see that this is a linked list problem with the current array that we have (pattern)
# Then, we need to find the duplicate number in the array
# This is done using fLoyd algortihm to solve this problem. Such explanation can be found in the notes

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0

        # Found the meeting pointin the looped linked list
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # Go simultaneously from the head and the meeting point and they are going to
        # meet at the start of the circle.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow