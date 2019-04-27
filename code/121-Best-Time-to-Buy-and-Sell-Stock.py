class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_num = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] < min_num:
                min_num = prices[i]
            else:
                current = prices[i] - min_num
                if current > result:
                    result = current
        return result
