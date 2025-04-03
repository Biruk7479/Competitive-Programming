class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum=0
        i=0
        max_av=float('-inf')
        while i+k <= len(nums):
            if i==0:
                for j in range(k):
                    cur_sum=cur_sum+nums[j]
                max_av=max(max_av, cur_sum/k)
            else:
                cur_sum=cur_sum-nums[i-1]+nums[i+k-1]
                max_av=max(max_av, cur_sum/k)
            i+=1
        return max_av


