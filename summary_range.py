from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        exist = []
        final = []
        for num in nums:
            if not exist:
                exist.append(num)
            # num 4
            # [0, 1, 2]
            elif exist[-1] + 1 == num:
                exist.append(num)

            elif exist[-1] + 1 != num:
                if exist[0] != exist[-1]:
                    final.append(str(exist[0]) + "->" + str(exist[-1]))
                    # 0 -> 2
                else:
                    final.append(str(exist[0]))
                exist=[]
                exist.append(num)
        if exist[0] != exist[-1]:
            final.append(str(exist[0]) + "->" + str(exist[-1]))
        else:
            final.append(str(exist[0]))
        return final


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
