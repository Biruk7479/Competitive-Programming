class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numWaterBottles = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            numWaterBottles += newBottles
            numBottles = newBottles + (numBottles % numExchange)
        return numWaterBottles


solution = Solution()
numBottles = 9
numExchange = 3
result = solution.numWaterBottles(numBottles, numExchange)
print(result)
