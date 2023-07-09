from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = nums[0]
        count = 0
        index = 0
        while index < len(nums):

            if nums[index] == check:
                count += 1
            else:
                check = nums[index]
                count = 1

            if count > 2:
                nums.pop(index)
                count -= 1
            else:
                index += 1
        return len(nums)


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
