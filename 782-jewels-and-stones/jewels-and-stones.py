from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      counter = Counter(stones)
      s=set(jewels)
      num=0
      for  i in s:
        if i in counter:
            num+=counter[i]
      return num      


