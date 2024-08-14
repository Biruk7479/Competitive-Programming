class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min=nums[-1]
        for num in range(len(nums)-1):
            if abs(nums[num]) <= abs(min):
                min = nums[num]
        if (min*-1 in nums) and (min in nums):
            min=abs(min)
        return min     
                

            