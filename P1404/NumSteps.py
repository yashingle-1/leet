class Solution:
    def numSteps(self, s: str) -> int:
        """
        Count the number of steps to reduce a binary string to '1'.
        If even (ends with 0): divide by 2 (remove last bit)
        If odd (ends with 1): add 1 (which creates carries)
      
        Args:
            s: Binary string representation of a positive integer
          
        Returns:
            Number of steps needed to reduce to '1'
        """
        carry = False  # Track if there's a carry from addition
        steps = 0  # Total number of operations
      
        # Process the binary string from right to left, excluding the first bit
        # s[:0:-1] reverses the string and excludes the first character
        for bit in s[:0:-1]:
            # Handle carry from previous addition
            if carry:
                if bit == '0':
                    bit = '1'  # 0 + carry = 1
                    carry = False  # No more carry
                else:
                    bit = '0'  # 1 + carry = 0, carry remains
          
            # If current bit is 1, the number is odd
            if bit == '1':
                steps += 1  # Add 1 to make it even
                carry = True  # Addition creates a carry
          
            steps += 1  # Divide by 2 (shift right)
      
        # If there's still a carry after processing all bits,
        # we need one more division step
        if carry:
            steps += 1
          
        return steps
