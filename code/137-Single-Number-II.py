class Solution:

    def singleNumber(self, nums: 'List[int]') -> 'int':

        num_map = {}
        for v in nums:
            if v not in num_map:
                num_map[v] = 1
            else:
                num_map[v] += 1

        for key in num_map:
            if num_map[key] == 1:
                return key
