from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Function to find first occurrence
        def findFirst():
            left = 0
            right = len(nums) - 1
            ans = -1  # Store answer if found

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid        # Save index
                    right = mid - 1  # Move left to find earlier target

                elif nums[mid] < target:
                    left = mid + 1   # Target is on right side

                else:
                    right = mid - 1  # Target is on left side

            return ans


        # Function to find last occurrence
        def findLast():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid       # Save index
                    left = mid + 1  # Move right to find later target

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans


        # Return both positions
        return [findFirst(), findLast()]