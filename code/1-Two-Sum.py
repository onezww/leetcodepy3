class Solution:
    '''
    LeetCode第一道题目，使用hashmap解题，时间复杂度O(n), 空间复杂度O(n)
    '''

    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        num_map = {}
        for i, v in enumerate(nums):
            if target - v in num_map:
                return [num_map[target - v], i]
            else:
                num_map[v] = i
        return []
