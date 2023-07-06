from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass


s = Solution()
print(s.permute([5, 4, 6, 2]))

"""
[[5,4,6,2],[5,4,2,6],[5,6,4,2],[5,6,2,4],[5,2,4,6],[5,2,6,4],[4,5,6,2],[4,5,2,6],[4,6,5,2],[4,6,2,5],
[4,2,5,6],[4,2,6,5],[6,5,4,2],[6,5,2,4]
,[6,4,5,2],[6,4,2,5],[6,2,5,4],[6,2,4,5],[2,5,4,6],[2,5,6,4],[2,4,5,6],[2,4,6,5],[2,6,5,4],[2,6,4,5]]
"""


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i, n in enumerate(nums):
            if n in C:
                C[n].append(i)
            else:
                C[n] = [i]
        M = max([len(i) for i in C.values()])
        return min([i[-1] - i[0] for i in C.values() if len(i) == M]) + 1


