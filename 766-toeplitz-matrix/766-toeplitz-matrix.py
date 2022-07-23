class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j)
                
                if (i+1) < (len(matrix)) and (j+1) < len(matrix[0]) and matrix[i+1][j+1]!= matrix[i][j]:
                    return False
        return True