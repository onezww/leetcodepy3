class Solution:

    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) < 3:
            return []

        nums.sort()
        result = set()
        for i, v in enumerate(nums):
            if i > 1 and v == nums[i - 1]:
                continue

            map_nums = dict()
            offset_sum = 0 - v
            for j in nums[i + 1:]:
                if offset_sum - j in map_nums:
                    result.add((v, offset_sum - j, j))
                else:
                    map_nums[j] = 1
        return list(map(list, result))
