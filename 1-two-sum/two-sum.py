
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         num_to_index = {}
        
         for i, num in enumerate(nums):
            number = target - num
            
            if number in num_to_index:
                return [num_to_index[number], i]
            
            num_to_index[num] = i
        
         return []