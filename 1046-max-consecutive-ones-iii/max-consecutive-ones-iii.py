class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       max_w=0
       l=0
       zeros=0
       n=len(nums)

       for r in range(n):
         if nums[r]==0:
            zeros+=1
         while zeros > k:
            if nums[l]==0:
                zeros -= 1
            l+=1
         max_w=max(max_w, r-l+1)
       return max_w
            