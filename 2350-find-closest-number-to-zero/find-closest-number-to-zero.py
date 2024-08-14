class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min=nums[0]
        for num in range(len(nums)):
            if abs(nums[num]) <= abs(min):
                min = nums[num]
        if (min*-1 in nums) and (min in nums):
            min=abs(min)
        return min     
                

            