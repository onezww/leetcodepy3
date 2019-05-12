class Solution:

    def singleNumber(self, nums: 'List[int]') -> 'int':
        sum = 0
        for v in nums:
            sum ^= v
        return sum
