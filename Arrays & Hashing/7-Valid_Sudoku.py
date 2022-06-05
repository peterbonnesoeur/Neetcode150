
# . Easy to iunderstand solution where we just check the lines, columns and squares using dict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        logRows = collections.defaultdict(set)
        logColumns = collections.defaultdict(set)
        logSquares = collections.defaultdict(set)

        for row_index in range(9):
            for column_index in range(9):
                if board[row_index][column_index] == ".":
                    continue

                if (board[row_index][column_index] in logRows[row_index] or \
                   board[row_index][column_index] in logColumns[column_index] or \
                   board[row_index][column_index] in logSquares[(row_index//3, column_index//3)]):
                    return False

                logColumns[column_index].add(board[row_index][column_index])
                logRows[row_index].add(board[row_index][column_index])
                logSquares[(row_index//3, column_index//3)].add(board[row_index][column_index])

        return True


# Other solution, much more efficient since we just go trhough the sudiku, record the sets of positions and
def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i//3,j//3,c)]
        return len(seen) == len(set(seen))

#c, j and  i, c are in this order to distinguisdh the row and columns (ex : ('4', 4) and (4, '4').)

#In a more gruesome way, we can convert this code in :

def isValidSudoku(self, board: List[List[str]]) -> bool:
        return 1 == max(list(collections.Counter(
        x
        for i, row in enumerate(board)
        for j, c in enumerate(row)
        if c != '.'
        for x in ((c, i), (j, c), (i//3, j//3, c))
    ).values()) + [1] )