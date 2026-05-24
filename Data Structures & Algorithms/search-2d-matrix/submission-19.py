class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix[0]) * len(matrix)) - 1
        rows = len(matrix)
        cols = len(matrix[0])

        while l <= r:
            mid = (r - l) + l // 2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] < target:
                l = mid + 1
            elif matrix[r][c] > target:
                r = mid - 1
            else:
                return True
        return False