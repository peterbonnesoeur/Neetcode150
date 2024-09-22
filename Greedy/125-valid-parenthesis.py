import heapq
from copy import deepcopy

#TO REDO
class Solution:
    def checkValidString(self, s: str) -> bool:
        # represent the range of parenthesis,
        # Either left_min to left_max
        left_min, left_max = 0,0

        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1

            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0

        return left_min == 0







    def checkValidString_OLD(self, s: str) -> bool:
        stack = []
        def stringSearch(s, stack, case= 0):
            # print(stack, s, case)
            for i,item in enumerate(s):
                if item =="(":
                    stack.append(item)
                elif item == ")":
                    if len(stack)>0:
                        prev_item = stack.pop()
                        if prev_item == ")":
                            return False
                    else:
                        return False
                else:
                    return stringSearch(s[i+1:], deepcopy(stack), 1) or \
                           stringSearch("(" + s[i+1:], deepcopy(stack),2) or \
                           stringSearch(")" + s[i+1:], deepcopy(stack), 3)

            if len(stack) == 0:
                return True
            else:
                return False

        return stringSearch(s, stack)