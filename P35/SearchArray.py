from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0                    # Start pointer at the beginning of the array
        right = len(nums) - 1       # End pointer at the last index of the array

        while left <= right:        # Keep searching while there is still a valid range
            mid = (left + right) // 2  # Find the middle index to check (integer division)

            if nums[mid] == target:    # If middle value is exactly the target
                return mid             # Target found, return its index
            elif nums[mid] < target:   # If middle value is less than target
                left = mid + 1         # Move left pointer to the right of mid (target must be bigger)
            else:                       # If middle value is greater than target
                right = mid - 1        # Move right pointer to the left of mid (target must be smaller)

        return left                    # Target not found, left points to correct insert position
