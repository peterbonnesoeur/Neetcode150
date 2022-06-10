from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        Map = {"}": "{", ")":"(", "]":"["}

        for item in s:
            if item not in Map:
                stack.append(item)
                continue
            if not stack or stack[-1] != Map[item]:
                return False

            stack.pop()
        return not stack