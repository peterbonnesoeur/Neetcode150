# 1 - make thebase answer list
# 2 -iterate through the list
# 3 - if the current element is superior to the ones in the stack, update res iteratively

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append(i)
        return res