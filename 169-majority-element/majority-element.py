class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h=defaultdict(int)
        for i in range(len(nums)):
                h[nums[i]]+=1
        for num in h:
             if h[num] > len(nums) // 2:
                return num

                
                # majority = None
                #         count = 0

                #         for num in nums:
                #             if count == 0:
                #                 majority = num
                #                 count += 1
                #             else:
                #                 if num != majority:
                #                     count -= 1
                #                 else:
                #                     count += 1
                        
                #         return majority                