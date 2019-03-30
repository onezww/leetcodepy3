class Solution:

    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0

        length = 1
        ptmp = nums[0]
        for v in nums:
            if v == ptmp:
                continue
            else:
                length += 1
                ptmp = v
                nums[length - 1] = v
        return length
