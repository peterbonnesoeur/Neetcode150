from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operation_set = {"+", "-", "*", "/"}
        operations_stack = deque()
        val_stack = deque()

        for token in tokens:
            if token in operation_set:
                operations_stack.append(token)
                prev_op = True
            else:
                val_stack.append(int(token))

        print(val_stack, operations_stack)
        res = val_stack.popleft()
        length = len(val_stack)
        #print(res, val_stack)
        for i in range(length):
            #print(val_stack, operations_stack)

            operation = operations_stack.popleft()
            val = val_stack.popleft()

            print(res, val, operation)
            if operation == "*":
                res *= val
            elif operation == "/":
                res = int(val / res)
            elif operation == "-":
                res -= val
            elif operation == "+":
                res += val

            print("_", res, val, operation)

        return res
