class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       #####two pointers####
       left=0
       right=len(numbers)-1
       s=0
       while left < right:
        s=numbers[left]+numbers[right]
        if s<target:
            left+=1
        elif s>target:
            right-=1
        else:
            return [left+1,right+1]