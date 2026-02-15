class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1  # Start from the last character of each string
        carry = 0                       # Initialize carry to 0
        res = []                        # Result list to store digits (we will join later)
        
        # Loop until both strings are done and no carry left
        while i >= 0 or j >= 0 or carry:
            # Get current digits, if index < 0 then use 0
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            
            # Binary sum of digits + carry
            total = x + y + carry
            
            # Append current digit (0 or 1) to result
            res.append(str(total % 2))
            
            # Update carry (0 or 1)
            carry = total // 2
            
            # Move to next left digit
            i -= 1
            j -= 1
        
        # Reverse result to get correct order and join as string
        return ''.join(res[::-1])
