class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d=[]
        output=[]
        for i in nums:
            d.append(i**2)
        i=0
        j=len(d)-1
        while i<=j:
            if d[i]>d[j]:
                output.append(d[i])
                i+=1
            else:
                output.append(d[j])
                j-=1
        return output[::-1]        

            
        