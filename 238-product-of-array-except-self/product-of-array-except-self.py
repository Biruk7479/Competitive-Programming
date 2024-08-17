class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            left_mult=1
            right_mult=1
            length=len(nums)
            left_arr=[0]* length
            right_arr=[0]* length
            

            for i in range(length):
                j = -i-1
                left_arr[i]=left_mult
                left_mult*=nums[i]
                right_arr[j]=right_mult
                right_mult*=nums[j]



            return [l*r for l,r in zip(left_arr,right_arr)]    

        
        


        