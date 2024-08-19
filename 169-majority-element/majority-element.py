class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h=defaultdict(int)
        for i in range(len(nums)):
                h[nums[i]]+=1
        for num in h:
             if h[num] > len(nums) // 2:
                return num