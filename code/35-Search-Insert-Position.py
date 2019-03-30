class Solution:

    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return 0

        i = 0
        j = len(nums) - 1

        while i <= j:

            mid = (i + j) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        if i < 0:
            return 0
        elif i >= len(nums):
            return len(nums)

        if nums[i] > target:
            return i
        else:
            return i + 1
