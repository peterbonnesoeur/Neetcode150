# Mathmaticlally enhanced.The sum of the possibility for the 2 previous results
# give the right solution.
# Could also use a dfs if memory was not an issue and the depth of the tree was limited.


class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n

        n1, n2 = 2, 3

        for i in range(4, n):
            temp = n1 + n2
            n1 = n2
            n2 = temp

        return n1 + n2
