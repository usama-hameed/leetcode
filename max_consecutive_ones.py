from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_num = max(max_num, count)
                count = 0
        return max(max_num, count)


s = Solution()
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1,1,1,1]))
