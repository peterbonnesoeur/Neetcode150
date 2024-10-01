class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def setCrossZeroes(i, j):
            print(i,j)
            for row in range(len(matrix)):
                if row!= i:
                    if matrix[row][j] == 0:
                        continue
                    matrix[row][j] = None
            for col in range(len(matrix[0])):
                if col != j:
                    if matrix[i][col] == 0:
                        continue
                    matrix[i][col] = None

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    setCrossZeroes(i,j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0


        
        