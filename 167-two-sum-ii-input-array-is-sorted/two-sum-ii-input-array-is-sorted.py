class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {} 
        output = []
        
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num in d:
                output.append(d[num]+1)  # Index of the complement
                output.append(i+1)  # Current index
                break  # Exit if we found the pair
            d[numbers[i]] = i  # Store the index of the current number
        
        return sorted(output)