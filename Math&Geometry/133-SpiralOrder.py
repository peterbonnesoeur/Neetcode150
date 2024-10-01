class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def giveList(currMatrix):
            print(currMatrix)
            if len(currMatrix) == 0:
                return []
            elif len(currMatrix) == 1:
                return currMatrix[0]
            elif len(currMatrix[0]) == 0:
                return []
            elif len(currMatrix[0]) == 1:
                return [row[0] for row in currMatrix]

            res = []
            for i in range(len(currMatrix[0])):
                res.append(currMatrix[0][i])
            
            for i in range(1, len(currMatrix)):
                res.append(currMatrix[i][-1])
            
            for i in range(len(currMatrix[0])-2, -1,-1):
                res.append(currMatrix[-1][i])
            
            for i in range(len(currMatrix)-2, 0, -1):
                res.append(currMatrix[i][0])
            return res + giveList([row[1:-1] for row in currMatrix[1:-1]])
        
        return giveList(matrix)