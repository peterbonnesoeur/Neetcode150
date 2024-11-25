# This is a dynamic programming problem.
# Basically, one needs to understand the dynmaic of the robot first
# We are restraining our interval of movement at each iteration. That is the little trick
# Then, we start from the smallest subset and expand it in the x direction first
# then in the y direction.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]
