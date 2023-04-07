from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        final = {}
        pivit = int(len(nums)/2)

        for num in nums:
            if num in final:
                final[num] += 1
                if final[num] > pivit:
                    return num
            else:
                final[num] = 1

        # res = [k for k, v in final.items() if v > pivit]
        # return res[0]


s = Solution()
print(s.majorityElement([1]))
