from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exist = {}

        for num in nums:
            if num in exist:
                exist[num] = exist[num] + 1
                # print(exist[num])
                if exist[num] >= 2:
                    return True
                # else:
                #     exist[num] += 1
            else:
                exist[num] = 1
        return False


s = Solution()
print(s.containsDuplicate([1,2,3,4]))
