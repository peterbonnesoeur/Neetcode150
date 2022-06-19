from collections import deque
class Solution:

    Use dynamic programing to generate all the variations.

    #The trick is to say that n_open is the number of open parenthesis we have.
    # n_close is the number of close parenthesis we have.
    # and n_open >= n_open

    # The stopping criteria is n_open == n_close == n

    # Hence here, we justuse those to rewind thestack and addclosing or opened parenthesis.

    # the result is just a list of all theses variations

    # DFS approach - iterative
    def generateParenthesis(self, n: int) -> List[str]:
        open_n, closed_n, result = n, n, []
        self.dfs(open_n, closed_n, "", result)
        return result

    def dfs(self, open_n, closed_n, parenthesis_string, result):
        if closed_n < open_n:
            return
        if open_n == closed_n == 0:
            result.append(parenthesis_string)
            return
        if open_n > 0:
            self.dfs(open_n -1, closed_n, parenthesis_string + "(", result)
        if closed_n > 0:
            self.dfs(open_n, closed_n - 1,  parenthesis_string +")", result)


    # Stack based approach -> dfs in the big scheme of things
    def generateParenthesis_(self, n: int) -> List[str]:
        stack = deque()
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append("".join(stack))

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        #print(res)

        return res
