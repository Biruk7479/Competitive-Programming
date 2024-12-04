class Solution:
        def canMakeSubsequence(self, str1: str, str2: str) -> bool:
                i, j = 0, 0
                n1, n2 = len(str1), len(str2)
                while i < n1 and j < n2:
                    if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                        j += 1  # Match found, move to the next character in
                    i += 1  # Always move to the next character in str1
                return j == n2
