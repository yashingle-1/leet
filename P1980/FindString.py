class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Create a bitmask to track which counts of "1"s exist in the input
        # If bit i is set, it means there's a string with i ones in nums
        ones_count_mask = 0
      
        # For each binary string, count its ones and mark that count in the mask
        for binary_string in nums:
            ones_count = binary_string.count("1")
            ones_count_mask |= 1 << ones_count
      
        # Get the length of the binary strings
        string_length = len(nums)
      
        # Find the first count of ones that doesn't exist in the input
        # Check each possible count from 0 to n
        for ones_count in range(string_length + 1):
            # Check if this count of ones is NOT present in the mask
            # (mask >> ones_count & 1) gets the bit at position ones_count
            # XOR with 1 inverts it (0 becomes 1, 1 becomes 0)
            if (ones_count_mask >> ones_count & 1) ^ 1:
                # Create a string with 'ones_count' ones followed by zeros
                return "1" * ones_count + "0" * (string_length - ones_count)
