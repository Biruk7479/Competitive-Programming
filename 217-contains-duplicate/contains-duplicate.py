class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
                return True
        return False                    