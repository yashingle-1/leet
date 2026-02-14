class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        
        # Create DP table (triangle)
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        
        # Pour champagne into top glass
        dp[0][0] = poured
        
        # Process row by row
        for r in range(query_row):
            for c in range(len(dp[r])):
                
                # If glass overflows
                overflow = max(0, dp[r][c] - 1) / 2
                
                # Add overflow to next row glasses
                dp[r + 1][c] += overflow
                dp[r + 1][c + 1] += overflow
        
        # Glass cannot hold more than 1
        return min(1, dp[query_row][query_glass])