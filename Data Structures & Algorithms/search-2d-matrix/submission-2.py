class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL = len(matrix)
        colL = len(matrix[0])
        totalL = rowL * colL
        l , r = 0 , totalL - 1

        while l <= r:
            mid = l +(r - l) // 2
            rowP = mid // colL
            colP = mid % colL

            if matrix[rowP][colP] > target:
                r -= 1
            elif matrix[rowP][colP] < target:
                l += 1
            else:
                return True
        return False
        