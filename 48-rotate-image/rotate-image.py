class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mylist = [row[:] for row in matrix]
        n=len(matrix)
        for i in range(n):
            for j in range(n):
             matrix[i][j]=mylist[-j-1][i]