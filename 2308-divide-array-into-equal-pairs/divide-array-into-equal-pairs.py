class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}  
        for i in nums:  
            if i in d:  
                d[i] += 1  
            else:  
                d[i] = 1  
        for count in d.values():  # Iterate over values, not keys
                if count % 2 != 0:
                    return False
        return True 

                               