class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = False
        for i in range(len(matrix)):
            if target in matrix[i]:
                a = True
                break

        return a