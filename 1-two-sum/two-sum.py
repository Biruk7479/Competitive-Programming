class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]]=i
        for i in range(len(nums)):
            number=target-nums[i]
            if number in h and h[number]!=i:
                return[i,h[number]]  