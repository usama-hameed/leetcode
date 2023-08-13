from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for index, value in enumerate(nums):
            if index + 1 < len(nums):
                if value > nums[index - 1] and value > nums[index + 1]:
                    return index
            elif value > nums[index-1]:
                return index
        return 0

s = Solution()
print(s.findPeakElement([1]))