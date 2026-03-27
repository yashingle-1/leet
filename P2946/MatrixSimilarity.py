class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        """
        Check if matrix remains the same after k cyclic shifts.
        Even rows shift left, odd rows shift right.
      
        Args:
            mat: 2D matrix of integers
            k: Number of positions to shift
          
        Returns:
            True if matrix is similar after shifts, False otherwise
        """
        # Get the number of columns in the matrix
        num_cols = len(mat[0])
      
        # Iterate through each row with its index
        for row_idx, row in enumerate(mat):
            # Check each element in the current row
            for col_idx, element in enumerate(row):
                # For odd-indexed rows (1, 3, 5...), check right shift
                if row_idx % 2 == 1:
                    # Calculate position after right shift with wraparound
                    shifted_position = (col_idx + k) % num_cols
                    if element != mat[row_idx][shifted_position]:
                        return False
              
                # For even-indexed rows (0, 2, 4...), check left shift
                if row_idx % 2 == 0:
                    # Calculate position after left shift with wraparound
                    # Adding num_cols ensures positive result for modulo
                    shifted_position = (col_idx - k + num_cols) % num_cols
                    if element != mat[row_idx][shifted_position]:
                        return False
      
        # All elements match their shifted positions
        return True