from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        max_sum = 0
        final = {}
    

s = Solution()
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
