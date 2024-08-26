class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[]
        i=0
        j=len(nums)-1
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                output.append(nums[i]**2)
                i+=1
            else:
                output.append(nums[j]**2)
                j-=1
        output.reverse()        
        return output   

            
        