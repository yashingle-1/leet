class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a = s.count('a')       # Count total 'a's in string (initial deletions if we remove all 'a')
        deletions = total_a           # Worst case: remove all 'a's
        count_b = 0                   # Count of 'b's seen so far

        for char in s:
            if char == 'b':
                count_b += 1          # 'b' may need to be deleted later if 'a' appears after it
            else:  # char == 'a'
                total_a -= 1          # One less 'a' remains to consider for deletion
            # Minimum deletions at this point:
            # Either remove all 'a's after current point OR all 'b's before
            deletions = min(deletions, count_b + total_a)

        return deletions
