from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      counter = Counter(stones)
      num=0
      for  i in jewels:
        if i in counter:
            num+=counter[i]
      return num      


