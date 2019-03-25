class Solution:

    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':

        if len(nums) < 4:
            return []

        nums.sort()
        result = set()
        for i, v in enumerate(nums):
            if i > 1 and v == nums[i - 1]:
                continue

            three_sum = target - v
            offset = i + 1
            for j, v2 in enumerate(nums[offset:]):
                index2 = j + offset
                if index2 > offset + 1 and v2 == nums[index2 - 1]:
                    continue

                two_sum = three_sum - v2
                map_nums = {}
                for v3 in nums[index2 + 1:]:
                    if two_sum - v3 in map_nums:
                        result.add((v, v2, two_sum - v3, v3))
                    else:
                        map_nums[v3] = 1

        return list(map(list, result))
