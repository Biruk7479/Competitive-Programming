class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k=0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k]=nums[i]
        #         k+=1
        # return k

        j=len(nums)-1
        while(j>=0):
            if nums[j]==val:
                nums.pop(j)
            j-=1
        return len(nums)
            