#The trick here is to use the indexing of the matrix as a list to flatten the matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)*len(matrix[0]) - 1
        in_length = len(matrix[0])

        while l <= r:
            m = l + ((r - l) // 2) # (l + r) // 2 can lead to overflow
            a, b = m//in_length, m%in_length

            if matrix[a][b] > target:
                r = m - 1
            elif matrix[a][b] < target:
                l = m + 1
            else:
                return True
        return False


#In depth solution that is taking first a row search then a column search.
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False