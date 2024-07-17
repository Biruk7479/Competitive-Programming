class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        result = []
        for char in str(num):
            result.append(int(char))
        return result