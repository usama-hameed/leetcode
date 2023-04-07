from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        original_nums = nums.copy()
        done = False
        final=[]
        final.append(original_nums[:])
        start = 0
        while not done:
            if start == len(nums) - 1:
                start = 0
            else:
                val = original_nums.pop(start)
                start = start + 1
                original_nums.insert(start, val)
                # print(nums, original_nums)
                if nums == original_nums:
                    done = True
                else:
                    print(original_nums)
                    final.append(original_nums[:])
        return final


s = Solution()
print(s.permute([5,4,6,2]))

"""
[[5,4,6,2],[5,4,2,6],[5,6,4,2],[5,6,2,4],[5,2,4,6],[5,2,6,4],[4,5,6,2],[4,5,2,6],[4,6,5,2],[4,6,2,5],
[4,2,5,6],[4,2,6,5],[6,5,4,2],[6,5,2,4]
,[6,4,5,2],[6,4,2,5],[6,2,5,4],[6,2,4,5],[2,5,4,6],[2,5,6,4],[2,4,5,6],[2,4,6,5],[2,6,5,4],[2,6,4,5]]
"""