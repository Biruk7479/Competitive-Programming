from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
            freq = Counter(words)  # Count each 2-letter word
            length = 0             # To hold total length of palindrome
            center_used = False    # To allow only one central palindromic word

            for word in list(freq.keys()):  # Loop over all unique words
                rev = word[::-1]            # Get the reversed word (e.g., 'ab' -> 'ba')

                if word != rev:  # Case 1: Non-palindromic pairs like 'ab' and 'ba'
                    if rev in freq:
                        pairs = min(freq[word], freq[rev])
                        length += pairs * 4   # Each pair adds 4 characters
                        freq[word] -= pairs   # Decrease counts of both
                        freq[rev] -= pairs
                else:  # Case 2: Palindromic words like 'gg'
                        pairs = freq[word] // 2
                        length += pairs * 4       # Each pair still adds 4 characters
                        freq[word] -= pairs * 2
                        if freq[word] > 0 and not center_used:
                                length += 2
                                center_used = True

            return length
