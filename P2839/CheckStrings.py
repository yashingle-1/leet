class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        """
        Check if two strings can be made equal by swapping characters at even or odd positions.
      
        The key insight is that characters at even indices can only be swapped with other 
        characters at even indices, and characters at odd indices can only be swapped with 
        other characters at odd indices.
      
        Args:
            s1: First string to compare
            s2: Second string to compare
          
        Returns:
            True if the strings can be made equal through allowed swaps, False otherwise
        """
        # Extract and sort characters at even positions (0, 2, 4, ...) from both strings
        s1_even_chars_sorted = sorted(s1[::2])
        s2_even_chars_sorted = sorted(s2[::2])
      
        # Extract and sort characters at odd positions (1, 3, 5, ...) from both strings
        s1_odd_chars_sorted = sorted(s1[1::2])
        s2_odd_chars_sorted = sorted(s2[1::2])
      
        # Both even and odd position characters must match after sorting
        return (s1_even_chars_sorted == s2_even_chars_sorted and 
                s1_odd_chars_sorted == s2_odd_chars_sorted)