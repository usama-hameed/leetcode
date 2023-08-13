from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0

        for hour in hours:
            if hour >= target:
                count += 1
        return count


s = Solution()
print(s.numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))
