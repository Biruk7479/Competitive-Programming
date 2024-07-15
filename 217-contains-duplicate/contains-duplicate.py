from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       d=Counter(nums)
       for j in d.values():
        if j > 1:
         return True
       return False 
