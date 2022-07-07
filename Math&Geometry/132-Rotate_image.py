class Solution:

    # Smart solution for image rotation : 1- inverse the image
    # 2 -inverse x and y axis of each element.
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    # trickier solution :
    # 1- take the topLeft element as a save and iterate through the restrained
    # matrix and replace iteratively (closed square rotated by small icrements until we reach 90 degrees)

    def rotate_(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # push things.

        l, r = 0, len(matrix) - 1

        while l < r:

            for i in range(r - l):
                top = l
                bottom = r

                topLeft = matrix[top][top + i]

                matrix[top][top + i] = matrix[bottom - i][top]

                matrix[bottom - i][top] = matrix[bottom][bottom - i]

                matrix[bottom][bottom - i] = matrix[top+i][bottom]

                matrix[top + i][bottom] = topLeft

            r -=1
            l+=1