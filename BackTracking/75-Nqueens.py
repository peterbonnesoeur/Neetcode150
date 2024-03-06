
# The rough sketch
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        subset = []
        result = []
        def dfs(depth, col = [], left_diagonal= [], right_diagonal = []):
            # print(depth)
            if depth >= n:
                result.append(list(subset))
                return
            current_left_diagonal = [i - 1 for i in left_diagonal if i > 0]
            current_right_diagonal = [i + 1 for i in right_diagonal if i < n]
            no_goes = set(col + current_left_diagonal + current_right_diagonal)

            for i in range(n):
                if i in no_goes:
                    continue
                temp_line = ["."]*n
                temp_line[i] = "Q"            
                col.append(i)
                current_right_diagonal.append(i)
                current_left_diagonal.append(i)
                subset.append("".join(temp_line))
                dfs(depth+1,col, current_left_diagonal, current_right_diagonal)
                subset.pop()
                col.pop()
                current_right_diagonal.pop()
                current_left_diagonal.pop()
            return
            
        dfs(0)
        return result


# The more opimized solution
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens, xy_diff, xy_sum):
            p = len(queens)  # p indicates the current row.
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])

        result = []
        DFS([], [], [])
        # Convert numerical results to the board representation
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

# Example usage
sol = Solution()
