class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Check if all '1's in the binary string form exactly one contiguous segment.
      
        The logic: If the pattern '01' exists in the string, it means there's a '0' 
        followed by a '1', indicating that '1's appear again after being interrupted 
        by '0's, which means multiple segments exist.
      
        Args:
            s: A binary string containing only '0's and '1's
          
        Returns:
            True if all '1's form a single contiguous segment, False otherwise
        """
        # Check if the substring '01' exists in the string
        # If '01' is not found, all '1's are contiguous (return True)
        # If '01' is found, there are multiple segments of '1's (return False)
        return '01' not in s
