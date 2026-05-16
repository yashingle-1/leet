from typing import List
from collections import Counter


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        """
        Determines if the given array is "good".
      
        A "good" array of length n+1 contains:
        - Each integer from 1 to n-1 exactly once
        - The integer n exactly twice
      
        Args:
            nums: List of integers to check
          
        Returns:
            bool: True if the array is "good", False otherwise
        """
        # Count the frequency of each number in the array
        frequency_counter = Counter(nums)
      
        # Calculate n (the maximum expected value)
        # Since a good array has length n+1, n = length - 1
        n = len(nums) - 1
      
        # Check two conditions:
        # 1. The number n appears exactly twice
        # 2. All numbers from 1 to n-1 appear at least once (exactly once for a valid "good" array)
        has_n_twice = frequency_counter[n] == 2
        has_all_numbers = all(frequency_counter[i] == 1 for i in range(1, n))
      
        return has_n_twice and has_all_numbers
