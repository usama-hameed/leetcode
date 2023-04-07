from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        not_exist = 0
        exist = []
        for index, num in enumerate(nums):
            if num in nums[index+1:] or num in exist:
                exist.append(num)
            else:
                not_exist = num
        return not_exist


s = Solution()
print(s.singleNumber([2,2,1]))
