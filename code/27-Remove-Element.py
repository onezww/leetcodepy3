class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        offset = 0
        length = 0
        for i, v in enumerate(nums):
            if v != val:
                length += 1
                nums[i - offset] = v
            else:
                offset += 1

        return length
