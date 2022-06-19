# use thekey as the closure poin to check the validity of the parenthesis.
# If the entry is not there, we just ad it to the stack. At each iteration, we pop the stack and check if the
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        Map = {"}": "{", ")":"(", "]":"["}

        for item in s:
            if item not in Map:
                stack.append(item)
                continue
            elif not stack or stack[-1] != Map[item]:
                return False

            stack.pop()
        return not stack