from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:           # Check for empty matrix
            return False

        # Step 1: Find the correct row
        row = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:  # Target is in this row
                row = i
                break
        else:
            return False                           # Target is not in any row

        # Step 2: Search in the row (binary search for optimization)
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:        # Found target
                return True
            elif matrix[row][mid] < target:       # Go right
                left = mid + 1
            else:                                  # Go left
                right = mid - 1

        return False                               # Target not found
