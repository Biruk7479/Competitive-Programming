class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h=defaultdict(int)
        for i in range(len(nums)):
                h[nums[i]]+=1
        for i in range(len(nums)):
            if h[nums[i]]>len(nums)//2:
             return nums[i]