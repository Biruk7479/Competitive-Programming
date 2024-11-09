class Solution:
    def minOperations(self, s: str) -> int:

        n = len(s)
        changes_for_pattern1 = 0
        changes_for_pattern2 = 0

        for i in range(n):
            expected_char_pattern1 = '0' if i % 2 == 0 else '1'  # Pattern "010101..."
            expected_char_pattern2 = '1' if i % 2 == 0 else '0'  # Pattern "101010..."

            # Count mismatches for each pattern
            if s[i] != expected_char_pattern1:
                changes_for_pattern1 += 1
            if s[i] != expected_char_pattern2:
                changes_for_pattern2 += 1

        # Return the minimum changes required
        return min(changes_for_pattern1, changes_for_pattern2)
