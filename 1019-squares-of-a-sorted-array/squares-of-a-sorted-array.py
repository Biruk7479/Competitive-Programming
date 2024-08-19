class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d=[]
        for i in nums:
            x=d.append(i**2)
        return sorted(d)    
            
        