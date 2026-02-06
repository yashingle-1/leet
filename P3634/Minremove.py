from typing import List

class Solution:
    def minimumRemovals(self, nums: List[int], k: int) -> int:
        nums.sort()                         # Sort array so we can easily track min and max
        n = len(nums)                       # Store total number of elements
        left = 0                            # Left pointer represents minimum element of window
        max_len = 1                         # Store size of largest balanced subarray

        for right in range(n):              # Right pointer represents maximum element of window
            
            # If window becomes unbalanced
            while nums[right] > nums[left] * k:
                left += 1                   # Move left pointer to shrink window
            
            # Calculate current valid window size
            current_len = right - left + 1
            
            # Update largest balanced window found so far
            max_len = max(max_len, current_len)

        return n - max_len                  # Minimum removals = remove elements outside best window
