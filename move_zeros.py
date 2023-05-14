from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0

        for r in range(len(nums)):
            if nums[r]:
                # l = 1, r = 2
                # [1,0,0,3,12]
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        print(nums)


s = Solution()
s.moveZeroes([0,1,0,3,12])
