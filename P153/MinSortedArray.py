from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #We compare middle element with last element.
        left = 0                     # Start pointer
        right = len(nums) - 1        # End pointer

        while left < right:          # Continue until pointers meet
            mid = (left + right) // 2  # Find middle index

            if nums[mid] > nums[right]:
                # Minimum is in right half
                left = mid + 1
            else:
                # Minimum is in left half including mid
                right = mid

        return nums[left]            # Left will point to minimum