class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = -5001
        left=0
        right=len(nums)-1
        while left<right:
            middle=(left+right)//2
            if nums[middle]>nums[right]:
                left=middle+1
            else:
                right=middle
        return nums[left]

