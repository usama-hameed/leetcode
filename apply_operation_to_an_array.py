from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for index, value in enumerate(nums):
            if index + 1 < len(nums):
                if nums[index] == nums[index + 1]:
                    nums[index] = nums[index] * 2
                    nums[index + 1] = 0

        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums


s = Solution()
print(s.applyOperations([1,2,2,1,1,0]))
