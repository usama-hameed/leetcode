from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l


s = Solution()
print(s.removeElement([3,2,2,3], 3))
