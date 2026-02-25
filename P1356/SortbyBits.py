class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        Sort an array by the number of 1 bits in ascending order.
        If two numbers have the same number of 1 bits, sort them by value in ascending order.
      
        Args:
            arr: List of integers to be sorted
          
        Returns:
            List of integers sorted by bit count, then by value
        """
        # Sort the array using a custom key function
        # Primary key: count of 1 bits in binary representation
        # Secondary key: the number itself (for tie-breaking)
        return sorted(arr, key=lambda num: (num.bit_count(), num))
