class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        l , r = 0 , (rowLen * colLen) - 1

        while l <= r:
            mid = l + (r - l) // 2
            rowInd = mid // colLen
            colInd = mid % colLen
            if matrix[rowInd][colInd] > target:
                r = mid - 1
            elif matrix[rowInd][colInd] < target:
                l = mid + 1
            else: 
                return True
        return False
