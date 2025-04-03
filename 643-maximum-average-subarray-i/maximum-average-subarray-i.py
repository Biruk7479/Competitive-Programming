class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum=0
        n = len(nums)

        for i in range(k):
            cur_sum+=nums[i]
            max_av=cur_sum/k
        for i in range(k,n):
            cur_sum+=nums[i]
            cur_sum-=nums[i-k]
            av=cur_sum/k
            max_av=max(max_av , av)
        return max_av
            


