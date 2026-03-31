class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        l, r = 0 , (rowLen * colLen) - 1


        while l <= r:
            mid = l + (r - l) // 2
            row = mid // colLen
            col = mid % colLen
            if matrix[row][col] > target:
                r -= 1
            elif matrix[row][col] < target:
                l += 1
            else:
                return True
        return False