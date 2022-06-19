#The goal here is to consider the stack as something that we can decrement/increment
#we keep the latest operations in it and we remove the val, process them in iteration.

#1 - we fill the stack with everything numerical
#2 - when there is an operation, use the poped element of the stack to perform the operation
#and add it to the existing stack
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]