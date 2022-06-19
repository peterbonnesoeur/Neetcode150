#The trick here is to actuaally use 2 stacks. The first one acts as the regular stack while the second one just keep the last mean value that it has stored.
# the storing system only consists in remberiong the smallest valueduring the push time

from collections import deque
class MinStack:

    def __init__(self):
        self.stack_ = deque()
        self.min_stack_ = deque()

    def push(self, val: int) -> None:
        if len(self.stack_) == 0:
            self.stack_.append(val)
            self.min_stack_.append(val)
        else:
            self.stack_.append(val)
            self.min_stack_.append(min(val, self.min_stack_[-1] if self.min_stack_ else val))

    def pop(self) -> None:
        self.stack_.pop()
        self.min_stack_.pop()

    def top(self) -> int:
        return self.stack_[-1]

    def getMin(self) -> int:
        return self.min_stack_[-1]
