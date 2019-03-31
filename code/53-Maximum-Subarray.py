class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        max_sum = nums[0]
        tmp_sum = nums[0]
        for v in nums[1:]:
            tmp_sum = max(tmp_sum + v, v)
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum
